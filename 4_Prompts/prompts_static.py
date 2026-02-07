from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

st.header('Reasearch Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summerise'):
    result = model.invoke(user_input)
    st.write(result.content)