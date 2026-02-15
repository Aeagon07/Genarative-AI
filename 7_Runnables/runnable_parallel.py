from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Tweet generation
prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}.",
    input_variables=['topic'],
)

# Post Generation
prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}.",
    input_variables=['topic'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet': RunnableSequence(prompt1, model, parser),
        'post': RunnableSequence(prompt2, model, parser),  
    }
)  

res = parallel_chain.invoke({'topic': 'Artificial Intelligence'})

print("Generated Tweet: ", res['tweet'])
print("Generated LinkedIn Post: ", res['post']) 
