import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from datetime import datetime
from langchain_core.tools import tool



load_dotenv()

REPO_ID = os.getenv("REPO_ID")


@tool
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """This tool is used to get the current time in given format.

    Args:
        format (str): The format to use.
    """
    return datetime.now().strftime(format)

tools = [get_current_time]

llm = HuggingFaceEndpoint(repo_id=REPO_ID,
                          temperature=0)

chat_model = ChatHuggingFace(llm=llm)

chat_model_with_tools = chat_model.bind_tools(tools=tools,
                                              tool_choice="auto")





# prompt="""You are a Ai assistent ,You have to give the answers to the users questions."""

# response=chat_model_with_tools.invoke([SystemMessage(content=prompt),HumanMessage(content="what is the current time?")])

# print(response,type(response.content))