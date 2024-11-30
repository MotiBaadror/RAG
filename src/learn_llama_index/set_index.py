import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage, Document, \
    Settings
from llama_index.core.node_parser import MarkdownElementNodeParser
from llama_parse import LlamaParse

from dir_configs import add_rootpath
from dotenv import load_dotenv
load_dotenv()


def get_files(data_path):
    files = os.listdir(add_rootpath(data_path))
    files = [os.path.join(add_rootpath(data_path), file) for file in files if file!='.DS_Store']
    return files


def get_index(storage_path, data_path, force=False, use_llamaparse=False, return_documents=False):
    if use_llamaparse:
        storage_path = os.path.join(storage_path, 'llamaparse')
    PERSIST_DIR = add_rootpath(storage_path)
    if not os.path.exists(PERSIST_DIR) or force:
        print('Storage not found, creating new storage')
        # load the documents and create the index
        if use_llamaparse:
            print('using llamaparse parsing')
            files = get_files(data_path)

            documents = LlamaParse(result_type="markdown").load_data(
                files
            )
        else:
            documents = SimpleDirectoryReader(add_rootpath(data_path)).load_data()

        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        print('loading existing storage')
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    return index

def get_nodeids_from_index(index):
    docwise_nodeids = []
    ref_doc_info = index.ref_doc_info
    for doc_id in ref_doc_info:

        node_ids = index.ref_doc_info[doc_id].to_dict()['node_ids']
        docwise_nodeids.append(node_ids)
    return docwise_nodeids

def get_document_from_index(index):
    node_id = get_nodeids_from_index(index)[0][0]
    d = Document(text=index.docstore.get_document(node_id).get_content())
    return [d]

def get_recursive_query_engine(documents):
    node_parser = MarkdownElementNodeParser(llm=Settings.llm, num_workers=4)
    nodes = node_parser.get_nodes_from_documents(documents)
    base_nodes, objects = node_parser.get_nodes_and_objects(nodes)
    recursive_index = VectorStoreIndex(nodes=base_nodes + objects, llm=Settings.llm)

    recursive_query_engine = recursive_index.as_query_engine(
        similarity_top_k=5, llm=Settings.llm
    )
    return recursive_query_engine