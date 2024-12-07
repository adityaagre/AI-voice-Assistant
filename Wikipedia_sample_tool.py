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
from langchain_core.tools import StructuredTool
from dotenv import load_dotenv
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_core.tools import tool
from langchain.tools import BaseTool
from math import pi
from typing import Union


# class CircumferenceTool(BaseTool):
#     name = "Circumference calculator"
#     description = "use this tool when you need to calculate a circumference using the radius of a circle"
#
#
# def _run(self, radius: Union[int, float]):
#     return float(radius) * 2.0 * pi
#
#
# def _arun(self, radius: int):
#     raise NotImplementedError("This tool does not support async")

@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

load_dotenv()  # take environment variables from .env.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


#
# # @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b
#

# Let's inspect some of the attributes associated with the tool.
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

# multiplier = StructuredTool.from_function(func=multiply)
tools = load_tools(["wikipedia", add], llm=llm)
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

