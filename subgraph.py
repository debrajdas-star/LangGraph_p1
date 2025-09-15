from langgraph.graph import StateGraph,MessagesState,START

def call_model(state:MessagesState):
    print("subgraph")
    return {"message":"Hi from the subgraph"}

subgraph_buiilder=StateGraph(MessagesState)

subgraph_buiilder.add_node("call_model",call_model)
subgraph_buiilder.set_entry_point("call_model")
subgraph_buiilder.set_finish_point("call_model")
subgraph=subgraph_buiilder.compile()

builder=StateGraph(MessagesState)


def call_main(state:MessagesState):
    print("supergraph")
    return {"message":"Hi from the main(Parent) graph"}

builder.add_node("call_supergraph",call_main)
builder.add_node("subgraph",subgraph)

builder.add_edge(START,"call_supergraph")
builder.add_edge("call_supergraph","subgraph")
builder.set_finish_point("subgraph")

graph=builder.compile()

response = graph.invoke({"messages":"Hi i am debraj"})

print(response)
