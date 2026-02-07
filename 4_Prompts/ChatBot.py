from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

chat_history = []

model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name = "llama-3.3-70b-versatile",
    temperature=0.2
)

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    if user_input == 'Messi or Ronaldo':
        print("AI: Ronaldo Always!")
    else :
        res = model.invoke(chat_history)
        chat_history.append(res.content)
        print(f"AI: {res.content}")

print(chat_history)

        
    