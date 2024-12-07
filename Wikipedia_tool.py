# import langchain
# from langchain.chat_models import ChatOpenAI
# from langchain import PromptTemplate, LLMChain
# import openai
import os
from groq import Groq
from langchain_groq import ChatGroq
# import langchain_openai
# from langchain_openai import ChatOpenAI
import dotenv
import wikipedia

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

from langchain.agents import load_tools, initialize_agent, AgentType

llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")



tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True ## It shows its thinking when verbose is true.
)

question = "What is the square root of the population of the capital of the country where the Olympic Games were held in 2016 ?"
question2 = "Who won maharashtra elections november 2020?"
question3= "Who won maharashtra elections november 2024?"
prompt = """You are a query agent. You have a wikipedia tool at yur disposal. Please use Wikipedia to answer any questions you do not know the answers to. This includes any recent events you do not know about."""
prompt = prompt + question3
print(agent.invoke(prompt))

