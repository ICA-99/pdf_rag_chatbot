from langchain_community.vectorstores import FAISS


def save_vectorstore(chunks, embeddings, path):

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(path)

    print("Vector database saved")


def load_vectorstore(path, embeddings):

    vectorstore = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore