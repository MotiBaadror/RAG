from components.prompts import prompt_template
from components.set_index import get_index
from components.set_llm import set_llm
from dto.configs import QueryConfig

if __name__ == '__main__':
    config = QueryConfig(model_name='llama3.1')
    set_llm(model=config.model_name)

    index = get_index(config.storage_path, config.data_path, use_llamaparse=True)

    query_engine = index.as_query_engine()


    while True:
        q = input('Write your query\n>>>')
        if q == 'q':
            break
        query = prompt_template.format(query= q)
        response = query_engine.query(query)
        print(response)

#     "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
#     "Which of the companies is potentially overvalued?"
#     "What is the shareholders’ equity for FinServ?"
