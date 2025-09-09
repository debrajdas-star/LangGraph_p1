import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

import requests

# ✅ Patch requests globally to disable gzip
old_request = requests.Session.request

def new_request(self, method, url, **kwargs):
    headers = kwargs.pop("headers", {})
    headers["Accept-Encoding"] = "identity"
    return old_request(self, method, url, headers=headers, **kwargs)

requests.Session.request = new_request
# from tools import tools

load_dotenv()

REPO_ID = os.getenv("REPO_ID")



llm = HuggingFaceEndpoint(repo_id=REPO_ID,
                          temperature=0)

chat_model = ChatHuggingFace(llm=llm)

# response=chat_model.invoke("Hi i am debraj")
# print(response.content)

# chat_model_with_tools = chat_model.bind_tools(tools=tools)





# prompt="""You are a Ai assistent ,You have to give the answers to the users questions."""

# response=chat_model_with_tools.invoke([SystemMessage(content=prompt),HumanMessage(content="what is the current time?")])

# print(response,type(response.content))