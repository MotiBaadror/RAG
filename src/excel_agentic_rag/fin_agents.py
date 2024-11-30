from llama_index.agent.openai import OpenAIAgent
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from pydantic import Field


def calculate_shareholder_equity(
        share_price: float = Field(
        description="Share price of the company <value>"
        ),
        total_outstanding_shares: int = Field(
        description="Total outstanding shares of the company price of the company <value>"
    )
    ) -> float:

    """return the shareholder equity, given share_price and total_outstanding share, this is same
     for company market capitalization"""
    return share_price*total_outstanding_shares


def calculate_eps(
        net_income: float= Field(
            description="net company income formated like <value> "
        ),
        outstanding_shares: int = Field(
            description="outstanding shares of the company formated like <value>"
        )
    ) -> float:
    """return EPS for given companies net income and total outstanding shares"""
    return net_income/outstanding_shares


def get_agents_from_fn(llm, fns):
    tools = [FunctionTool.from_defaults(fn=fn) for fn in fns]
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
    return agent


def get_tools_from_fns(fns):
    tools = [FunctionTool.from_defaults(fn=fn) for fn in fns]
    return tools


def get_agent_from_tools(llm, tools, context=None,max_iterations=10, react_agent=False):
    if context is None:
        print('No context is provided for tool')
    if react_agent:
        agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, max_iterations=max_iterations, context=context)
    else:
        agent = OpenAIAgent.from_tools(tools, llm=llm)
    return agent

