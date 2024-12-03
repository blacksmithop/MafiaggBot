from langchain_core.messages import HumanMessage
from mafiagg.chatbot.agent import get_graph
from mafiagg.helper.custom_exceptions import FailedToLoadAgent

try:
    graph = get_graph()
except FailedToLoadAgent:
    graph = None

def get_bot_response(user_query: str, user_id: int = None):
    if graph == None:
        return None
    config = {"configurable": {"thread_id": user_id}}
    user_message = [HumanMessage(user_query)]
    bot_response = graph.invoke({"messages": user_message}, config)
    bot_message = bot_response["messages"][-1].content
    return bot_message