from  langchain_community.document_loaders import PyPDFLoader



loader=PyPDFLoader("R Deep Learning Essentials.pdf")

docs=loader.load()
print(len(docs)) #170 bcz pdf contain 170 pages

print(docs[0]) # details about first page
 