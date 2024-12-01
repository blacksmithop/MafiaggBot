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


system_prompt = """Be a helpful assistant"""


# Define the function that calls the model
def call_model(state):
    messages = state["messages"]

    config = {"configurable": {"model_name": getenv("LLM_PROVIDER")}}
    model_name = config.get("configurable", {}).get("model_name", "openai")
    print(f"Model NAME: {model_name}")
    model = _get_model(model_name)
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}


# Define the function to execute tools
tool_node = ToolNode(tools)
