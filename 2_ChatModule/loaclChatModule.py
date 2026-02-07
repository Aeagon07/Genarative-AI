#  This is where you run your module locally
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# If your C drive is full then you can use the D drive also
os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id= 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task= 'text-generation',
    pipeline_kwargs= dict(
        temperature = 0.5,
        max_new_token = 100
    )
)

model = ChatHuggingFace(llm=llm)

res = model.invoke("What is Capital of India")

print(res.content)