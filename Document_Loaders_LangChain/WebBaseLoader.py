from langchain_community.document_loaders import WebBaseLoader

url="https://www.flipkart.com/canon-eos-r50-mirrorless-camera-body-rf-s-18-45-mm-f-4-5-6-3-stm/p/itm3bc65ea11d81b?pid=DLLGN2WBZ6JJS3JJ&lid=LSTDLLGN2WBZ6JJS3JJFZSEOW&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=en_M-af2rZ2a3LIgSwZsGS5fqiznRa0Hwus1NNirV4C7ejZqlkTFxLR3miFpje_Hnx1ZLUmceYRZQNpvfEsmgiG4w%3D%3D&ppt=hp&ppn=homepage&ssid=szr506juxc0000001756413618331"

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))

print(docs[0].page_content)