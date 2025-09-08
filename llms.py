import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from tools import tools

load_dotenv()

REPO_ID = os.getenv("REPO_ID")



llm = HuggingFaceEndpoint(repo_id=REPO_ID,
                          temperature=0)

chat_model = ChatHuggingFace(llm=llm)

chat_model_with_tools = chat_model.bind_tools(tools=tools)





# prompt="""You are a Ai assistent ,You have to give the answers to the users questions."""

# response=chat_model_with_tools.invoke([SystemMessage(content=prompt),HumanMessage(content="what is the current time?")])

# print(response,type(response.content))