from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

res = llm.invoke("What is Capital of India")

print(res)

# this is now outdated so please don't use the this code