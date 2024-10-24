import os

from llama_index.core import Document, VectorStoreIndex, StorageContext, load_index_from_storage

from dir_configs import add_rootpath
from learn_llama_index.set_llm import set_llm
from podcast_chatbot.data import parsed, episode_summary, parsed_summary


set_llm()

print(episode_summary[:100])



print(parsed_summary[:100])

start_of_transcript = [x.text for x in parsed_summary].index("Transcript") + 1
print(f"First line of the transcript: {start_of_transcript}")

documents = [Document(text=t.text) for t in parsed_summary[start_of_transcript:]]

PERSIST_DIR = add_rootpath("./storage/chatbot")
if not os.path.exists(PERSIST_DIR):
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("What does Jerry think about RAG?")
print(response)
# print(documents)


