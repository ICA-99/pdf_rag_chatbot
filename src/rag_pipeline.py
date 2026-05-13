from langchain_community.vectorstores import FAISS

from src.document_loader import load_documents
from src.text_splitter import split_documents


def process_pdf(pdf_path, embeddings):

    documents = load_documents(pdf_path)

    chunks = split_documents(documents)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def ask_question(question, vectorstore, chain):

    results = vectorstore.similarity_search(
        query=question,
        k=3
    )

    context = "\n\n".join([
        doc.page_content for doc in results
    ])

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content