from langchain_groq import ChatGroq


def load_llm():

    llm = ChatGroq(
        model="llama-3.1-8b-instant"
    )

    return llm