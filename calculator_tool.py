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
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent

prompt = hub.pull("hwchase17/openai-tools-agent")

load_dotenv()  # take environment variables from .env.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")


@tool
def add(first_int: int, second_int: int) -> int:
    "Add two integers."
    return first_int + second_int

@tool
def multiply(first_int: int, second_int: int) -> int:
    "Multiply two integers"
    return first_int*second_int

@tool
def exponentiate(base: int, exponent: int) -> int:
    "Exponentiate the base to the exponent power."

    return base**exponent

@tool
def add_to_notes(notes_to_add) :
    "If the user wants to add some text to their notes folder, you should pass that text here."
    file = open('user_notes.txt', 'w')
    file.write(notes_to_add)
    return None

@tool
def read_notes() :
    "If the user wants to read their notes folder. This will return the contents of the notes folder."
    file = open('user_notes.txt', 'r')
    text = file.read()
    return text



tools = [multiply, add, exponentiate, add_to_notes, read_notes]

# Construct the tool calling agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
#
agent_executor.invoke(
    {
        "input": "Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result"
    }
)

# agent_executor.invoke(
#     {
#         "input": "Add to my notes : 'Wash Car.'"
#     }
# )

agent_executor.invoke(
    {
        "input": "Read the contents of my notes file."
    }
)
