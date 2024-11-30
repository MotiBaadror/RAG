from components.query_engine import get_agent_from_query_engine_and_tools
from dto.configs import QueryConfig
from excel_agentic_rag.fin_agents import  get_tools_from_fns, \
     calculate_shareholder_equity,calculate_eps
from components.set_index import get_index
from components.set_llm import set_llm

def build_agent():
    config = QueryConfig()
    set_llm(model=config.model_name)

    index = get_index(config.storage_path, config.data_path, use_llamaparse=True)

    query_engine = index.as_query_engine()


    func_tools = get_tools_from_fns(fns=[calculate_shareholder_equity, calculate_eps])
    agent = get_agent_from_query_engine_and_tools(
        query_engine=query_engine,
        func_tools=func_tools
    )
    return agent


if __name__ == '__main__':

    agent = build_agent()
    while True:
        q = input('provide a prompt for me\n>>>')
        if q =='q':
            break
        final_prompt = f"{q},Go step by step, using a tool to do any math."
        try:
            response = agent.chat(final_prompt)
            print(response)
        except:
            pass
