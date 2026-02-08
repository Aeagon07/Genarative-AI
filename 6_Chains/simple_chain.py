from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variable= ['topic']
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name ="llama-3.1-8b-instant",
)

parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({'topic': 'Football'})

print(result)

chain.get_graph().print_ascii()