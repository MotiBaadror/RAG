from components.prompts import  get_prompts, update_prompt_in_engine
from components.set_index import get_index
from dto.configs import QueryConfig


def test_prompts():
    config = QueryConfig()
    index = get_index(data_path=config.data_path,storage_path=config.storage_path,use_llamaparse=config.use_llama_parse)
    query_engine = index.as_query_engine()
    get_prompts(query_engine)
    print('updated prompts')
    update_prompt_in_engine(query_engine=query_engine)
    get_prompts(query_engine)

