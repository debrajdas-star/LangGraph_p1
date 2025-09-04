from vectordb import retriever

print('Enter exit to exit...')
while(True):
    query=input("Enter your query:")
    if query.strip().lower()=='exit':
        print("Thanks for using")
        break
    docs=retriever.invoke(query)
    # print(len(docs))
    for k,doc in enumerate(docs):
        print(f"Document{k+1}:")
        print(doc.page_content)