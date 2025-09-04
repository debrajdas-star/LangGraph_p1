from langchain_community.document_loaders import DirectoryLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

folder_path='./docs'

loader=DirectoryLoader(path=folder_path,glob="**/*.txt",loader_cls=TextLoader)

docs=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)

all_splites=text_splitter.split_documents(docs)


embeddings=HuggingFaceEmbeddings(model_name = "sentence-transformers/all-mpnet-base-v2") #768 dims
