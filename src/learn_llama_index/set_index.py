import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage

from dir_configs import add_rootpath


def get_index(storage_path, data_path, force=False):
    PERSIST_DIR = add_rootpath( storage_path)
    if not os.path.exists(PERSIST_DIR) or force:
        print('Storage not found, creating new storage')
        # load the documents and create the index
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