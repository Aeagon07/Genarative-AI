from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='book',
    glob='*.pdf',
    loader_cls=PyPDFLoader,
)

# doc = loader.load()
doc = loader.lazy_load() # Instead of load() use the lazy_load()

# print(len(doc))
# print(doc[0].metadata)

# we have the 326 doc which are load at one time,

for document in doc:
    print(document.metadata)
