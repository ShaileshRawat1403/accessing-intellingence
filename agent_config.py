import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

def get_agent_executor():
    model = ChatGroq(
        model_name="llama3-70b-8192",  # ✅ Use current Groq-supported model
        temperature=0.7,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template(
        "Given the input: {input}, recommend 5 songs similar to the artists mentioned."
    )

    chain = (
        {"input": RunnablePassthrough()}
        | prompt
        | model
    )

    return chain
