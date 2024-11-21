from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_community.vectorstores import FAISS

import os
import streamlit as st


def create_vector_store(chunks):
    embeddings = NVIDIAEmbeddings(model="NV-Embed-QA")
    # Creates the vector store
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
    # Stores it locally
    vector_store.save_local("vector_store")