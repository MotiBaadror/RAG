from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from excel_agentic_rag.fin_agents import get_agents_from_fn, get_tools_from_fns, \
    get_agent_from_tools, calculate_shareholder_equity,calculate_eps
from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

model = 'llama3.2'
set_llm(model=model)

index = get_index(f"storage/codelon_data_{model}", "data/codelon_data", use_llamaparse=True)

query_engine = index.as_query_engine()


func_tools = get_tools_from_fns(fns=[calculate_shareholder_equity, calculate_eps])
finance_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="finance_data",
            description=(
                "A RAG engine with some basic facts about financial values for the companies"
            ),
            return_direct=False
    )
)
all_tools = func_tools+[finance_tool]
context = "If the user asks a question the you already know the answer to OR the user is making idle banter, just respond without calling any tools."


agent = get_agent_from_tools(llm=Settings.llm, tools=all_tools,max_iterations=10, context=context)
# prompt = "Which of the companies is potentially overvalued?"
# prompt = "Give me shareholder equity for FinServ company"
# prompt = "Give me share price for FinServ company, Go step by step, using a tool to do any math."
prompt = "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"
# final_prompt = f"{prompt}, use company tool to retrieve data and other tool for calculation"
final_prompt = f"{prompt}"


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
