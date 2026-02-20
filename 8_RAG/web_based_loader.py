from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt = PromptTemplate(
    template="Answer the Following question \n {question} from the following text \n {text}",
    input_variables=['question', 'text'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

url = 'https://amzn.in/d/0cnmcouD'
loader = WebBaseLoader(url)

# Here we just the single url you can use the list of urls as well

doc = loader.load()

chain = prompt | model | parser

res = chain.invoke({
    'question': 'What is product description?',
    'text': doc[0].page_content,
})

print(res)