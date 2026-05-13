from langchain_core.prompts import ChatPromptTemplate


def create_chain(llm):

    prompt = ChatPromptTemplate.from_messages([

        (
            "system",

            """
            You are a helpful AI assistant.

            Answer ONLY from the provided context.

            If answer is not present in context,
            say:

            "I don't know from the uploaded PDF."
            """
        ),

        (
            "human",

            """
            Context:
            {context}

            Question:
            {question}
            """
        )
    ])

    chain = prompt | llm

    return chain