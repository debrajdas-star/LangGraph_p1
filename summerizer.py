#In this module we will build a graph which has the chat summarizer features
from langchain_core.messages import RemoveMessage,HumanMessage
from llms import chat_model
from langgraph.graph import START,END,StateGraph
from langgraph.graph.message import add_messages,AnyMessage
from graph import memory
from typing import TypedDict,Annotated

class State(TypedDict):

    question: str
    summary: str
    answer: str
    messages: Annotated[list[AnyMessage],add_messages]

def chatbot(state: State):
    summary = state.get("summary","")
    question = state.get("question","")
    if summary:
        prompt = [HumanMessage(content=summary)] + state["messages"]
    else:
        prompt = state["messages"]

    response = chat_model.invoke(prompt+[HumanMessage(content=question)])
    answer = response.content
    print(answer)
    state["messages"] = [response]
    return state

def summarize(state: State):
    messages = state['messages']
    summary = state.get("summary","")

    if not summary:
        task = HumanMessage(content="summerize the above messages")
        response = chat_model.invoke(messages+[task])
        return_summary = response.content
    else:
        return_summary = summary
    
    deleted_messages =  [RemoveMessage(id=m.id) for m in messages[:-2]]

    state["summary"] = return_summary
    state["messages"] = deleted_messages

    return state

def should_summarize(state:State):
    if len(state['messages'])>5:
        return "summarize"
    return END

builder = StateGraph(State)
builder.add_node("chatbot",chatbot)
builder.add_node("summarize",summarize)

builder.add_edge(START,"chatbot")
builder.add_conditional_edges("chatbot",
                              should_summarize)
builder.add_edge("summarize",END)

graph_with_semmerizer = builder.compile(checkpointer=memory)