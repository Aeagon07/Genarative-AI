from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt = PromptTemplate(
    template="Suggest a joke about {topic}.",
    input_variables=['topic'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    tempalate="Explain the following joke - {text}.",
    input_variables=['text'],
)

chain = RunnableSequence(prompt, model, parser, prompt1, model, parser)

print(chain.invoke({'topic': 'Artificial Intelligence'}))