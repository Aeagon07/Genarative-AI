from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}.",
    input_variables=['text'],
)

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='llama-3.1-8b-instant',
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

# Conditions => if report size > 500 words trigger the summarization chain else,
# it just pass through the report_gen_chain output
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chian = RunnableSequence(report_gen_chain, branch_chain)

print(chian.invoke({'topic': 'Rusia vs Ukraine war'}))