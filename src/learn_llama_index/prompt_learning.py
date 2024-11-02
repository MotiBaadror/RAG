from dto.configs import QueryConfig
from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

set_llm()

config = QueryConfig(
    data_path='data/paul_gram_data'
)

index = get_index(
    data_path=config.data_path,
    storage_path=config.storage_path
)

retriever = index.as_retriever()
nodes = retriever.retrieve("Who is Paul Graham?")

print('nodes: ',nodes)