from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

st.set_page_config(page_title="Research Summarizer", layout="centered")

st.title("📄 Research Summarization Tool")
st.write("Paste your text below and get a concise AI-generated summary.")

# Input box (better than text_input for long text)
user_input = st.text_area("Enter your text", height=250)

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            prompt = f"""
            Summarize the following text clearly and concisely.
            Provide key points in bullet format.

            Text:
            {user_input}
            """

            response = llm.invoke(prompt)

            st.subheader("✅ Summary")
            st.write(response.content)
