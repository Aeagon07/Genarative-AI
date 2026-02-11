from langchain_groq import ChatGroq
from langchain_core import LLMChain
from langchain_core.prompts import PromptTemplate
import os

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catchy blog title about {topic}.",
)

# Creating LLMChain -> Simplest chain that help you to automate the task 
chain = LLMChain(llm=llm, prompt=prompt)

topic = input("Enter your topic: ")

output = chain.run({"topic": topic})

print("Generate Blog Title: ", output)