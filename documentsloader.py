from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

folder_path = './docs'

loader = DirectoryLoader(path=folder_path,
                         glob="**/*.pdf",
                         loader_cls=PyPDFLoader)

docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)





text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                               chunk_overlap=200,
                                               add_start_index=True)

all_splites = text_splitter.split_documents(docs)


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2") #768 dims
