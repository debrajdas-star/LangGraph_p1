from typing import TypedDict, Annotated
from llms import chat_model_with_tools, tools
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

# print(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state:State):

    return {"messages": [chat_model_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot",chatbot)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools",tool_node)


graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("tools","chatbot")

graph = graph_builder.compile()

# response=graph.invoke({"messages":"Hi i am debraj"})
# print(response)