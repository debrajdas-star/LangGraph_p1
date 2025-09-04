from langchain_core.vectorstores import InMemoryVectorStore
from documentsloader import embeddings,all_splites

vector_store=InMemoryVectorStore(embedding=embeddings)
vector_store.add_documents(all_splites)

retriever=vector_store.as_retriever(search_type="similarity",
    search_kwargs={"k": 3},)
