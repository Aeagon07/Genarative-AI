from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='Document Loaders/DL.pdf',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)


spliter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

docs = loader.load()

res = spliter.split_documents(docs)

print(res[0].page_content)
# It will return the list of chunks of text