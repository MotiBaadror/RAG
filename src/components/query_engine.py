from llama_index.core import Settings
from llama_index.core.tools import ToolMetadata, QueryEngineTool

from excel_agentic_rag.fin_agents import get_agent_from_tools


def get_agent_from_query_engine_and_tools(query_engine,func_tools):

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
    all_tools = func_tools + [finance_tool]
    context = "If the user asks a question the you already know the answer to OR the user is making idle banter, just respond without calling any tools."

    agent = get_agent_from_tools(llm=Settings.llm, tools=all_tools, max_iterations=10, context=context)
    return agent