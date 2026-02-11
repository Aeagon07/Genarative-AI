from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catchy blog title about {topic}.",
)

topic = input("Enter a Topic: ")

formated_prompt = prompt.format(topic=topic)

blog_title = llm.invoke(formated_prompt)

print("Generated Blog Title: ", blog_title.content)