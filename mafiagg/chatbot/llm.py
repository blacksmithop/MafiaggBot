from os import getenv
# TODO: Cache

PROVIDER = getenv("LLM_PROVIDER")

if PROVIDER == "ollama":
    try:
        from langchain_ollama.embeddings import OllamaEmbeddings
        from langchain_ollama.llms import OllamaLLM
    except ImportError:
        print("Please install the langchain-ollama package")
        exit(0)

    OLLAMA_URL = getenv("OLLAMA_URL")

    llm = OllamaLLM(base_url=OLLAMA_URL, model="kristada673/solar-10.7b-instruct-v1.0-uncensored")
    embeddings = OllamaEmbeddings(base_url=OLLAMA_URL, model="nomic-embed-text")

elif PROVIDER == "gemini":
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
    except ImportError:
        print("Please install the langchain-google-genai package")
        exit(0)

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        api_key=getenv("GOOGLE_API_KEY"),
        temperature=0,
        max_tokens=100,
        timeout=None,
        max_retries=2,
    )
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

elif PROVIDER == "openai":
    try:
        from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
    except ImportError:
        print("Please install the langchain-openai package")
        exit(0)

    llm = AzureChatOpenAI(
        deployment_name=getenv("GPT_DEPLOYMENT_NAME"),
        temperature=0,
        max_tokens=500,
    )
    underlying_embeddings = AzureOpenAIEmbeddings(
        azure_deployment=getenv("EMBEDDINGS_DEPLOYMENT_NAME"),
    )
# Use nodmodel2vece2vec and some AGI/Rasa?
# TODO: Tool calling

if __name__ == "__main__":
    print(len(embeddings.embed_query("Hi")))
    print(llm.invoke("Hi"))