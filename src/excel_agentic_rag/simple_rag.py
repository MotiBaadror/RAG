from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

model = 'llama3.2'
set_llm(model=model)

index = get_index(f"storage/codelon_data_{model}", "data/codelon_data", use_llamaparse=True)

query_engine = index.as_query_engine()


while True:
    q = input('Write your query\n>>>')
    if q == 'q':
        break
    response = query_engine.query('how many companies are there?')
    print(response)

#     "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
#     "Which of the companies is potentially overvalued?"
#     "What is the shareholders’ equity for FinServ?"
