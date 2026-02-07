from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder

# Chat Template
chat_temp = ChatMessagePromptTemplate([
    ('syetem', 'Your are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])

chat_history = []
# Load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readline())

print(chat_history)

# Create prompt
chat_temp.invoke({
    'chat_history': chat_history,
    'query': 'Where is my refund',
})