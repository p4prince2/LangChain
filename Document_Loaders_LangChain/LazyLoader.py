from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader


loader=DirectoryLoader(

path="Data Analytics",
    glob="*.pdf",
loader_cls=PyPDFLoader
)


docs=loader.lazy_load() # Generator ---> docs
for i in docs:
    print(i.metadata)

