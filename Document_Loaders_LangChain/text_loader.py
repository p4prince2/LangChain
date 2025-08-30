from langchain_community.document_loaders import TextLoader

loader=TextLoader("cricket.txt",encoding="utf-8")

docs=  loader.load()

print(docs)
print(type(docs)) #<class 'list'>
print(len(docs)) # 1
print("page_content--------->",docs[0].page_content)
print("metadata ------>",docs[0].metadata)