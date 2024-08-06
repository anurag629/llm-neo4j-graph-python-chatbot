import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# Create the LLM
llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model_name=st.secrets["OPENAI_MODEL"],
)

# Create the Embedding model
embedding = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)