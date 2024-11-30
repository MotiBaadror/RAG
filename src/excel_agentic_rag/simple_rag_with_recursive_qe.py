from components.set_index import get_index, get_document_from_index, get_recursive_query_engine
from components.set_llm import set_llm

model = 'llama3.1'
set_llm(model=model)

index = get_index(f"storage/codelon_data_{model}", "data/codelon_data", use_llamaparse=True)

documents = get_document_from_index(index)
query_engine = get_recursive_query_engine(documents=documents)


while True:
    q = input('Write your query\n>>>')
    if q == 'q':
        break
    response = query_engine.query(q)
    print(response)

#     "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
#     "Which of the companies is potentially overvalued?"
#     "What is the shareholders’ equity for FinServ?"
