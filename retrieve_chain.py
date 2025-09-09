from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from llms import chat_model as llm
from schemas import Products
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import requests

# ✅ Patch requests globally to disable gzip
old_request = requests.Session.request

def new_request(self, method, url, **kwargs):
    headers = kwargs.pop("headers", {})
    headers["Accept-Encoding"] = "identity"
    return old_request(self, method, url, headers=headers, **kwargs)

requests.Session.request = new_request

folder_path = './docs'

loader = DirectoryLoader(path=folder_path,
                         glob="**/*.pdf",
                         loader_cls=PyPDFLoader)

docs = loader.load()

docs_text = "\n".join(doc.page_content for doc in docs[19:25])

# print(docs_text)

parser = PydanticOutputParser(pydantic_object=Products)

prompt_template = """Read this following docs {docs} clearly and deeply and then give me the list of prodcts as much as you can only from this documents.
**Do not genereate any random data if the data is relevent then generate the data**
if no relearde data found then just return empty list
Return in this format:
{format_instructions} 
containing all the fields,if any data is incomplete just don't take that.
"""

prompt = PromptTemplate.from_template(
    template=prompt_template,
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm 

response = chain.invoke({"docs": docs_text})

print(response.content)