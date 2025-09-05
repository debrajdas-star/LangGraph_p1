from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from graph import graph

load_dotenv()

print("++++AI MODEL++++(press \"exit\" to get out of the chat)")
while(1):
    #When a new chat session will start we have to give a thread_id for each chat sesion.
    #And using the thread_id it will save all the state
    config = {"configurable": {"thread_id": "1"}}
    query: str = input('Enter:')
    if query.strip().lower() == 'exit':
        print("Thanks for using ...")
        break
    prompt = """You are a helpful assistant that can use tools to answer questions."""
    state = {"messages":[SystemMessage(content=prompt),HumanMessage(content=query)]}
    print(f'You:{query}')
    print('AI:', end='')
    #While invoking the graph we have to provide the config which the graph will follow.
    state=graph.invoke(state, config=config)
    print(state['messages'][-1].content)
    print("-----------",state)
    print()