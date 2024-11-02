from llama_index.core import SimpleDirectoryReader, Settings

from dir_configs import add_rootpath
from dto.configs import QueryConfig
from learn_llama_index.set_llm import set_llm

config  = QueryConfig(
    data_path='data/paul_gram_data'
)

set_llm()

documents = SimpleDirectoryReader(add_rootpath(config.data_path)).load_data()

# print(documents)

nodes = Settings.node_parser.get_nodes_from_documents(documents)
# print('Here is nodes\n')
# print(nodes)

from llama_index.core import StorageContext

# initialize storage context (by default it's in-memory)
storage_context = StorageContext.from_defaults()
storage_context.docstore.add_documents(nodes)