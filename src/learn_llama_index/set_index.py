import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_parse import LlamaParse

from dir_configs import add_rootpath
from dotenv import load_dotenv
load_dotenv()


def get_files(data_path):
    files = os.listdir( add_rootpath(data_path))
    files = [os.path.join(add_rootpath(data_path), file) for file in files]
    return files


def get_index(storage_path, data_path, force=False, use_llamaparse=False):
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