import operator
from langgraph.graph import StateGraph,START,END
# from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated


class State(TypedDict):

    value : Annotated[list[str],operator.add]


# def a(state:State):

#     print(f"adding A to {state['value']}")
#     return {"value": ["A"] }

# def b(state:State):

#     print(f"adding B to {state['value']}")
#     return {"value": ["B"] }

# def c(state:State):

#     print(f"adding C to {state['value']}")
#     return {"value": ["C"] }

# def d(state:State):

#     print(f"adding D to {state['value']}")
#     return {"value": ["D"] }

# builder = StateGraph(State)

# builder.add_node("a",a)
# builder.add_node("b",b)
# builder.add_node("c",c)
# builder.add_node("d",d)

# builder.add_edge(START,"a")
# builder.add_edge("a","b")
# builder.add_edge("a","c")
# builder.add_edge("b","d")
# builder.add_edge("c","d")
# builder.add_edge("d",END)

# graph = builder.compile()

# result = graph.invoke({"value":[]})

# print(result)

def a(state:State):

    print(f"adding A to {state['value']}")
    return {"value": ["A"] }

def b_1(state:State):

    print(f"adding B1 to {state['value']}")
    return {"value": ["B1"] }

def b_2(state:State):

    print(f"adding B2 to {state['value']}")
    return {"value": ["B2"] }

def c(state:State):

    print(f"adding C to {state['value']}")
    return {"value": ["C"] }

def d(state:State):

    print(f"adding D to {state['value']}")
    return {"value": ["D"] }

builder = StateGraph(State)

builder.add_node("a",a)
builder.add_node("b1",b_1)
builder.add_node("b2",b_2)
builder.add_node("c",c)
builder.add_node("d",d)

# builder.add_edge(START,"a")
# builder.add_edge("a","b1")
# builder.add_edge("a","c")
# builder.add_edge("b1","b2")
# builder.add_edge("b2","d")
# builder.add_edge("c","d")
# builder.add_edge("d",END)

#In this way the parallelism is not happening 
#To get the parallelism we have to do like this

builder.add_edge(START,"a")
builder.add_edge("a","b1")
builder.add_edge("a","c")
builder.add_edge("b1","b2")
builder.add_edge(["b2","c"],"d") # Now this will perform the parallelism
#This ["b2","c"],"d" -> signifies that before passing the state to d from c , c should wait for b2 to complete
#In other words both the b2 and c should run parallely
builder.add_edge("d",END)
graph = builder.compile()

result = graph.invoke({"value":[]})

print(result)