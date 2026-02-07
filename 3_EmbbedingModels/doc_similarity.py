# This is OpenAI Module with document similarity 

# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model= 'text-embedding-3-large',
# )

# document = [
#     "Virat Kohli is an Indian Cricketer known for his aggresive batting and leadership,",
#     "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
#     "MS Dhoni is former Indian Captain and famous for his calm demeanor and finishing skills."
# ]
# query = 'tell me about virat kohli'

# doc_emb = embeddings.embed_documents(document)
# query_emb = embeddings.embed_query(query)

# score = cosine_similarity([query_emb], doc_emb)[0]

# index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

# print(document[index])
# print("Similarity Socre is: ", score)


# Using the HuggingFaceEmbeddings

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "MS Dhoni is former Indian captain and famous for his calm demeanor and finishing skills."
]

query = "tell me about virat kohli"

doc_emb = embeddings.embed_documents(documents)
query_emb = embeddings.embed_query(query)

scores = cosine_similarity([query_emb], doc_emb)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Best Match:", documents[index])
print("Similarity Score:", score)
