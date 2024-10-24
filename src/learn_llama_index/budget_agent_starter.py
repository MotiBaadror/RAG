from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

model = 'llama3.2'
set_llm(model=model)

index = get_index(f"storage/llamaparse_budget_{model}", "data/llamaparse_budget")

query_engine = index.as_query_engine()

response = query_engine.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response)

