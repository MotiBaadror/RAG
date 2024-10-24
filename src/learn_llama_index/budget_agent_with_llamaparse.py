import os

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_parse import LlamaParse
from dotenv import load_dotenv
from dir_configs import add_rootpath
from learn_llama_index.set_llm import set_llm

model = 'llama3.2'
set_llm(model=model)
load_dotenv()


def get_index(storage_path, data_path='data/llamaparse_budget/2023_canadian_budget.pdf'):
    PERSIST_DIR = add_rootpath(storage_path)
    if not os.path.exists(PERSIST_DIR):
        print('Storage not found, creating new storage')
        # load the documents and create the index
        documents = LlamaParse(result_type="markdown").load_data(
            add_rootpath(data_path)
        )
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        print('loading existing storage')
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index


index2 = get_index(f"storage/llamaparse_cloud_{model}", "data/llamaparse_budget/2023_canadian_budget.pdf")
query_engine2 = index2.as_query_engine()

response2 = query_engine2.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response2)