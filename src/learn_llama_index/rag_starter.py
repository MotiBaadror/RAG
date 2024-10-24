from dotenv import load_dotenv
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from dir_configs import add_rootpath

load_dotenv()


llm = Ollama(model='llama3.2')


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

# def set_llm():
Settings.llm = llm

Settings.embed_model = OllamaEmbedding(
    model_name="llama3.2",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0},
)
Settings.llm.complete('Hi, How are you?')
documents = SimpleDirectoryReader(add_rootpath("data")).load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("I forgot my name, can you help me")
print(response)