from typing import TypedDict, Literal
from os import getenv
from langgraph.graph import StateGraph, END
from mafiagg.chatbot.nodes import call_model, should_continue, tool_node
from mafiagg.chatbot.state import AgentState
from mafiagg.helper.custom_exceptions import FailedToLoadAgent

if getenv("AGENT_VERBOSE") == "true":
    from langchain.globals import set_verbose, set_debug

    set_debug(True)


class GraphConfig(TypedDict):
    model_name: Literal["anthropic", "openai"]


def get_graph():
    try:
        workflow = StateGraph(AgentState, config_schema=GraphConfig)

        workflow.add_node("agent", call_model)
        workflow.add_node("action", tool_node)

        workflow.set_entry_point("agent")

        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {
                "continue": "action",
                "end": END,
            },
        )

        workflow.add_edge("action", "agent")

        graph = workflow.compile()
        return graph
    except Exception as e:
        raise FailedToLoadAgent(f"Failed to load agent due to: {str(e)}")
