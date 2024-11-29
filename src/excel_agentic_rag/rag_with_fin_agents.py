from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from excel_agentic_rag.fin_agents import get_agents_from_fn, get_tools_from_fns, \
    get_agent_from_tools, calculate_shareholder_equity,calculate_eps
from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

model = 'llama3.1'
set_llm(model=model)

index = get_index(f"storage/codelon_data_{model}", "data/codelon_data", use_llamaparse=True)

query_engine = index.as_query_engine()


# response = query_engine.query(
#     "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
# )
# print(response)
# response = query_engine.query(
#     "Which of the companies is potentially overvalued?"
# )
# print(response)
func_tools = get_tools_from_fns(fns=[calculate_shareholder_equity, calculate_eps])
finance_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="company_data",
            description=(
                "Financial information about the companies"
            ),
            # return_direct=False
    )
)
all_tools = func_tools+[finance_tool]

agent = get_agent_from_tools(llm=Settings.llm, tools=all_tools,max_iterations=50)
# prompt = "Which of the companies is potentially overvalued?"
# prompt = "Give me shareholder equity for FinServ company"
# prompt = "Give me share price for FinServ company, Go step by step, using a tool to do any math."
prompt = "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
# final_prompt = f"{prompt}, use company tool to retrieve data and other tool for calculation"
final_prompt = f"{prompt},Use company_data tool to get all required values for the computation, Go step by step, using a tool to do any math."



response = agent.query(final_prompt)
print(response)