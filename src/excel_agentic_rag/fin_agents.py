from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool


def shareholder_equity_fn(share_price:int,total_outstanding_shares):
    "Calculate the shareholder equity, given share_price and total_outstanding share "
    return share_price*total_outstanding_shares

def get_agents_from_fn(llm, fns):
    tools = [FunctionTool.from_defaults(fn=fn) for fn in fns]
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
    return agent

def get_tools_from_fns(fns):
    tools = [FunctionTool.from_defaults(fn=fn) for fn in fns]
    return tools

def get_agent_from_tools(llm, tools):
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
    return agent

