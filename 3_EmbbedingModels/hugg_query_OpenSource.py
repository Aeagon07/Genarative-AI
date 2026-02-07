from langchain_huggingface import HuggingFaceEmbeddings

embeding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the Capital of India"

vector = embeding.embed_query(text)

print(str(vector)) # get back the 384 dimensional vector
# Also you an send the document also instead of the text just use the embed_documents option