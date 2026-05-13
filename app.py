import os

import streamlit as st

from dotenv import load_dotenv

from src.embeddings import load_embeddings
from src.llm import load_llm
from src.rag_chain import create_chain
from src.rag_pipeline import process_pdf, ask_question


# =========================
# LOAD ENV
# =========================
load_dotenv()


# =========================
# CREATE UPLOAD FOLDER
# =========================
os.makedirs("uploads", exist_ok=True)


# =========================
# LOAD MODELS
# =========================
embeddings = load_embeddings()

llm = load_llm()

chain = create_chain(llm)


# =========================
# STREAMLIT UI
# =========================
st.title("PDF Chatbot")


# =========================
# PDF UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)


if uploaded_file:


    # save uploaded pdf
    pdf_path = f"uploads/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:

        f.write(uploaded_file.getbuffer())


    # =========================
    # CREATE VECTORSTORE ONCE
    # =========================
    if (
        "current_pdf" not in st.session_state
        or
        st.session_state.current_pdf != uploaded_file.name
    ):

        st.session_state.current_pdf = uploaded_file.name


        st.session_state.vectorstore = process_pdf(
        pdf_path=pdf_path,
        embeddings=embeddings
    )


    # delete uploaded pdf
    os.remove(pdf_path)


    st.success("PDF processed successfully")


    # =========================
    # USER QUESTION
    # =========================
    question = st.text_input(
        "Ask Question"
    )


    if question:


        answer = ask_question(
            question=question,
            vectorstore=st.session_state.vectorstore,
            chain=chain
        )


        st.write(answer)