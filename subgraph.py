import operator
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

class State(TypedDict):
    answer: str
    thinking: Annotated[list[str],operator.add]
    steps: Annotated[list[str],operator.add]


def a1(state:State):

    print(f"Adding A1 to steps. {state['steps']}")
    return {"steps":["A1"]}

s1_builder = StateGraph(State)
#Adding node to the subgraph1
s1_builder.add_node("a1",a1)
#Adding edge to the subgraph1
s1_builder.add_edge(START,"a1")
s1_builder.add_edge("a1",END)

#This is the subgraph1
subgraph1 = s1_builder.compile()

def a2(state:State):

    print(f"Adding A2 to steps. {state['steps']}")
    return {"steps":["A2"]}

s2_builder = StateGraph(State)
#Adding node to the subgraph2
s2_builder.add_node("a2",a2)
#Adding edge to the subgraph2
s2_builder.add_edge(START,"a2")
s2_builder.add_edge("a2",END)

#This is the subgraph2
subgraph2 = s2_builder.compile()

def top(state:State):
    return {"thinking":["Hi i am top"]}

def dispatch(state:State):
    return {}
def final_answer(state:State):
    # print("###########",state["steps"])
    print("generating the final answer")
    return {"answer":f"After cheking the steps,steps:{state["steps"]},it is determined that You are great at building subgraph"}

final_graph_builder = StateGraph(State)

final_graph_builder.add_node("top",top)
final_graph_builder.add_node("dispatch",dispatch)
final_graph_builder.add_node("subgraph1",subgraph1)
final_graph_builder.add_node("subgraph2",subgraph2)
final_graph_builder.add_node("final",final_answer)

final_graph_builder.add_edge(START,"top")
final_graph_builder.add_edge("top","dispatch")
final_graph_builder.add_edge("dispatch","subgraph1")
final_graph_builder.add_edge("dispatch","subgraph2")
final_graph_builder.add_edge("subgraph1","final")
final_graph_builder.add_edge("subgraph2","final")

final_graph = final_graph_builder.compile()

answer = final_graph.invoke({"steps":[]})
print(answer)