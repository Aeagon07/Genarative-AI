from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os

load_dotenv()

prompt = PromptTemplate(
    template="Write a 3 line summary of the following poem - \n {poem}",
    input_variables=['poem'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

doc = loader.load()

chain = prompt | model | parser 

res = chain.invoke({'poem': doc[0].page_content})

print(res)