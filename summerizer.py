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
    """This is the chatbot node
    
    here is there is summary then it will take both the summary \
    and the messages,but if it does not have the summary and only take the messages."""
    
    summary = state.get("summary","")
    question = state.get("question","")
    #here we are chekink if summary is present or not 
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
    """This is the for summerize the messages
    
    this nodes takes all the messages and then create a summary \
    and delete all the unecessary messages ,except the last two messages\
    or else it keeps it same."""

    messages = state['messages'] 
    summary = state.get("summary","")

    if not summary:
        task = HumanMessage(content="summerize the above messages")
        response = chat_model.invoke(messages+[task])
        return_summary = response.content
    else:
        return_summary = summary
    
    #deleting all the unnesary messages,except the  last two messages.
    deleted_messages =  [RemoveMessage(id=m.id) for m in messages[:-2]]

    state["summary"] = return_summary
    state["messages"] = deleted_messages

    return state

def should_summarize(state:State):
    """Conditional edge
    
    checks if the message length id greater than 5 then it will summerize of it will end."""
    if len(state['messages'])>5:
        return "summarize"
    return END


#buildig the graph
builder = StateGraph(State)

#adding all the nodes of the graph
builder.add_node("chatbot",chatbot)
builder.add_node("summarize",summarize)

#adding all the edges of the graph
builder.add_edge(START,"chatbot")
builder.add_conditional_edges("chatbot",
                              should_summarize)
builder.add_edge("summarize",END)

#creating the graph with the memory
graph_with_semmerizer = builder.compile(checkpointer=memory)