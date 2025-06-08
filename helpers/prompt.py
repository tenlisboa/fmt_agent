from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage, BaseMessage
from typing import List

def system(path: str, **kwargs) -> List[SystemMessage]:
    file_content = load(path)
    template = SystemMessagePromptTemplate.from_template(file_content)

    return template.format_messages(**kwargs)

def human(path: str, **kwargs) -> List[HumanMessage]:
    file_content = load(path)
    template = ChatPromptTemplate.from_template(file_content)

    return template.format_messages(**kwargs)

def load(file_path: str):
    with open(file_path) as f:
        file_content = f.read()

    return file_content
