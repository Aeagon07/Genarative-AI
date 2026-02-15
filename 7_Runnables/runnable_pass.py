from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template="Suggest a joke about {topic}.",
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}.",
    input_variables=['text'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser),
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(chain.invoke({'topic': 'Football'}))