from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage
from graph import graph
load_dotenv()

print("++++AI MODEL++++(press \"exit\" to get out of the chat)")
while(1):
    query: str=input('Enter:')
    if query.strip().lower()=='exit':
        print("Thanks for using ...")
        break
    prompt = """You are a helpful assistant that can use tools to answer questions."""
    state={"messages":[SystemMessage(content=prompt),HumanMessage(content=query)]}
    print(f'You:{query}')
    print('AI:',end='')
    response=graph.invoke(state)
    print(response["messages"][-1].content)
    print()