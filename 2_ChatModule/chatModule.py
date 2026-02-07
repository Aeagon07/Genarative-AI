# These are close-source models so they are not in working condition cause you have to pay to use them..
from langchain_openai import ChatOpenAI

# ChatOpenAI is inheriting from BaseChatOpenAI and it also inher. from BaseChatModel Which is mother class of everyting...

# meanwhile OpenAI is inheriting from the BaseOpenAI and here the mother class is BaseLLM..

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= 'gpt-4', temperature=1.5, max_completion_tokens=10)
# Cause these two features are very important while using the model, temperature decide how much randomness in your response and max_completion_token is decide how much token you want in your ouput 
res = model.invoke("What is the capital of India ?")

print(res)
# Here you see the lots of things rather than a plain text output like in lLM..

print(res.content) # for see the answer