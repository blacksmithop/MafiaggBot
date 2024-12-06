from functools import lru_cache
from langgraph.prebuilt import ToolNode
from mafiagg.chatbot.tools import get_wikipedia_information
from os import getenv

tools = [get_wikipedia_information]


@lru_cache(maxsize=4)
def _get_model(model_name: str):
    if model_name == "ollama":
        from mafiagg.chatbot.llm import get_ollama_models

        llm, _embeddings = get_ollama_models()
    elif model_name == "openai":
        from mafiagg.chatbot.llm import get_openai_models

        llm, _embeddings = get_openai_models()
    elif model_name == "google":
        from mafiagg.chatbot.llm import get_gemini_models

        llm, _embeddings = get_gemini_models()
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    model = llm.bind_tools(tools)
    return model


# Define the function that determines whether to continue or not
def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    # If there are no tool calls, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"


system_prompt = """You are a creative and intelligent AI assistant engaged in being a host to players of the game mafia.gg
During this process you will adopt the persona of Hannibal Lector while answering every query.
At no point will you divulge your identity as a Chatbot or AI assistant.
Attempt to give witty responses to user questions and keep the conversation flowing.
"""


# Define the function that calls the model
def call_model(state):
    messages = state["messages"]

    config = {"configurable": {"model_name": getenv("LLM_PROVIDER")}}
    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}


# Define the function to execute tools
tool_node = ToolNode(tools)
