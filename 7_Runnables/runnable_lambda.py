from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt = PromptTemplate(
    template="Suggest a joke about {topic}.",
    input_variables=['topic'],
)

def word_count(text):
    return len(text.split())

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    # 'word_count': RunnableLambda(word_count), 

    # another way
    'word_count': RunnableLambda(lambda x: len(x.split())),
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)

res = chain.invoke({'topic': 'AI'})

print("Generated Joke: ", res['joke'])
print("Word Count of the joke: ", res['word_count'])