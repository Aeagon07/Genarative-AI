from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on the {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template='Generate the 5 line summary form following text. \n {text}',
    input_variables=['text']
)

model = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
res = chain.invoke({'topic': 'Unemployment in India'})

print(res)

chain.get_graph().print_ascii()