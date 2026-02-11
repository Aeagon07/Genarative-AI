from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chains import RetrievalQA
import os

# load document 
loader = TextLoader("doc.text")
doc = loader.load()

# Split the document into smaller chunks
text_split = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
doc = text_split.split_documents(doc)

# Convert text into vectors and store in FAISS (Vector DB)
vectorstore = FAISS.from_documents(doc, HuggingFaceEmbeddings())

# Fetches relevant document
retriever = vectorstore.as_retriever()

# Model
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant", temperature=0.7)

# Retrieval QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)    

# Ask Question
query = "What is the main topic of the document?"
ans = qa_chain.run(query)

print("Answer: ", ans)