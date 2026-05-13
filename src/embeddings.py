from langchain_google_genai import GoogleGenerativeAIEmbeddings


def load_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    return embeddings