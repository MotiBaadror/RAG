from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from excel_agentic_rag.fin_agents import get_agents_from_fn, shareholder_equity_fn, get_tools_from_fns, \
    get_agent_from_tools
from learn_llama_index.set_index import get_index
from learn_llama_index.set_llm import set_llm

model = 'llama3.2'
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
func_tools = get_tools_from_fns(fns=[shareholder_equity_fn])
finance_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="company_data",
            description=(
                "A RAG system for finance information about various companies"
            ),
    )
)
all_tools = func_tools+[finance_tool]

agent = get_agent_from_tools(llm=Settings.llm, tools=all_tools)
# prompt = "Give me shareholder equity for FinServ company"
# prompt = "Give me share price for FinServ company, Go step by step, using a tool to do any math."
prompt = "What would the EPS be for Techcorp if there is a 3 for 1 stock split?"

response = agent.query(prompt)
print(response)