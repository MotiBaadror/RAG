from learn_llama_index.set_index import get_index

index = get_index( "storage/llamaparse_budget", "data/llamaparse_budget")

query_engine = index.as_query_engine()

response = query_engine.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response)

