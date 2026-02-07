# System Message => Dynamic 
# You are a welfare {domain} expert

# Human Message => Dynamic
# Explain about {Topic}

# When you want to create something like this where your system and human messages both are dynamic in nature..

from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

# chat_temp = ChatPromptTemplate(
#     [
#         SystemMessage(content='You are a helpful {domain} expert'),
#         HumanMessage(content='Explain in simple terms, what is {topic}')
#     ]
# )

# Instead of above lines you use these structure
chat_temp = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}'),
])

prompt = chat_temp.invoke({
    'domain': 'Cricket',
    'topic': 'No Ball'
})

print(prompt)

# Here you get weird out put, it not pass the values we assign for domain and topic cause the behaviour of the ChatPromptTemplate is different than the PromptTemplate..
# this is the uncertainty in this langague..