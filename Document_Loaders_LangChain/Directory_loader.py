from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader=DirectoryLoader(

path="Data Analytics",
    glob="*.pdf",
loader_cls=PyPDFLoader
)


docs=loader.load()


print(len(docs)) # 947 total pages of all book

print(docs[0])