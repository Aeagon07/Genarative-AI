from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
)

parser1 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['postive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Structure of Branch Chain
# RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default chain
# )

# You uses the lambda for real time logic implementilambda x: "could not find sentiment"
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser1),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser1),
    # this is not the chain, but you have to implement chain here..
    # lambda x: "could not find sentiment" 
    RunnableLambda(lambda x: "could not find sentiment")
)
# Here you uses the Runnable Lambda for converting the lambda to runnable lambda

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()