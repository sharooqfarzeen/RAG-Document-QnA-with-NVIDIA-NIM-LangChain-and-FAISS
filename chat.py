from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

import os
import streamlit as st


def get_response(context, user_question, chat_history):
    prompt_template = """
    You are provided with context extracted from multiple documents. The documents were uploaded as pdf documents. All of the text
    in the pdf were clubbed together and vectorized. 
    
    The end of each pdf is marked by the sentence "End of document."
    
    Answer the provided user question based on the provided context and previous chat history as accurately and 
    comprehensively as possible. If the answer is not available in the context or previous chat history, respond with 
    "The answer is not available in the provided documents."

    Make sure to:
    - Combine relevant information from different documents if needed.
    - If the documents don't contain relevant information, avoid guessing or providing incorrect answers.
    - Always reference details from the context, previous chat history and user input when forming your answer.

    Context from multiple documents:
    {context}

    Previous Chat History:
    {chat_history}

    Question:
    {user_question}

    Answer:
    """
    
    # Setting model to be used
    model = ChatNVIDIA(model="nvidia/llama-3.1-nemotron-70b-instruct", nvidia_api_key=st.session_state["NVIDIA_API_KEY"])
    
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    
    chain = create_stuff_documents_chain(llm=model, prompt=prompt)
    
    response = chain.invoke({"context": context, "chat_history": chat_history, "user_question": user_question})
    
    return response