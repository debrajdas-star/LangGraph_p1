from typing import TypedDict, Annotated
from llms import chat_model_with_tools
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver
from tools import tools
# print(tools)

#created a in memorysaver for savig all the states belongs to a particular "thread_id"
memory = InMemorySaver()


class State(TypedDict):

    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state:State):

    response = chat_model_with_tools.invoke(state["messages"])
    return {"messages": [response]}


graph_builder.add_node("chatbot",chatbot)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools",tool_node)


graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("tools","chatbot")

#while compiling the graph we have to provide te memory as the checkpointer params.
#The graph rememners which memory it has to use for saving the same thread states.
graph = graph_builder.compile(checkpointer=memory)


# response=graph.invoke({"messages":"Hi i am debraj"})
# print(response)