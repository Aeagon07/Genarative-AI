from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st 
import os 
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name ="llama-3.1-8b-instant",
    # temperature=0.2
)

st.header('Reasearch Tool')

# Creating few Dropdowns 
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Template
template = load_prompt('template.json')

# Old Hardcore Formate
# template = PromptTemplate(
#     template= """You are an expert research explainer. Your task is to summarize the research paper titled "{papertitle}" in a {explanationstyle} style and {explanation_length} length.

# 1. Mathematical Details:
#    - Include relevant mathematical equations if present in the paper.
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
#    - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with "Insufficient information available".

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['papertitle', 'explanationstyle', 'explanation_length']
# )

# Fill the placeholder
# prompt = template.invoke({
#     'papertitle': paper_input, 
#     'explanationstyle': style_input,
#     'explanation_length': length_input,
# })
# You can use the chaining also  

if st.button('Summerize'):
    chain = template | model
    res = chain.invoke({
        'paper_input': paper_input, 
        'style_input': style_input,
        'length_input': length_input,
    })
    # res = model.invoke(prompt) => No need to write this line in chaining 
    st.write(res.content) 