from langchain_core.tools import tool
from datetime import datetime
from vectordb import get_retriever
from localmemory import events, Event



@tool
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """This tool is used to get the current time in given format.

    Args:
        format (str): The format to use.
    """
    return datetime.now().strftime(format)

@tool
def rag_tool(query:str) -> str:
    """This tool is used to retrieve some related documents
    
    Args:
        format (str): This will be the query

    Output:
        returns the a str of all the page content of related docs.
    """

    retriever = get_retriever()
    docs = retriever.invoke(query)
    result = ""
    for doc in docs:
        result += (doc.page_content + "\n")
    return result

@tool
def add_event(event_data:Event) -> Event:
    """This tool is used to create a event

    returns the Event details
    """

    events[event_data.id] = Event
    return Event

@tool
def show_all_events() -> list[Event]:
    """This tool is used to get all the  events

    returns a list of all events
    """
    all_events = [event for event in events.values()]

    return all_events

#List of all the tools
tools = [get_current_time,rag_tool,add_event,show_all_events]
