from typing import TypedDict, Literal
from langchain.globals import set_verbose, set_debug

set_debug(True)
from langgraph.graph import StateGraph, END
from mafiagg.chatbot.nodes import call_model, should_continue, tool_node
from mafiagg.chatbot.state import AgentState


class GraphConfig(TypedDict):
    model_name: Literal["anthropic", "openai"]


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

if __name__ == "__main__":

    def stream_graph_updates(user_input: str):
        for event in graph.stream({"messages": [("user", user_input)]}):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        except Exception as e:
            print(e)
            exit(0)
