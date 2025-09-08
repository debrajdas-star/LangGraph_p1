from langchain_core.vectorstores import InMemoryVectorStore
from documentsloader import embeddings,all_splites


_VECTORDB=None

def get_vectordb():
    """This function give the vectordb from cached"""

    global _VECTORDB

    if not _VECTORDB:
        vector_store = InMemoryVectorStore(embedding=embeddings)    
        vector_store.add_documents(all_splites)
        _VECTORDB = vector_store

    return _VECTORDB

def get_retriever():
    """This function give the retriever of the vector db"""

    vector_store = get_vectordb()
    retriever = vector_store.as_retriever(search_type="similarity",
                                      search_kwargs={"k": 3},)
    
    return retriever