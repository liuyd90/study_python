from langchain_openai import OpenAI
from langchain_community.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("hi")

chat_model.invoke("")
