
# To run: `chainlit run basic.py`

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

import chainlit as cl

# Langchain config
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "BasicAgent"

# Ollama
# os.environ['OPENAI_API_BASE'] = 'http://localhost:11434/v1'
# os.environ['OPENAI_MODEL_NAME'] = 'openhermes'  # Adjust based on available model
# os.environ['OPENAI_API_KEY'] = 'NA'

# Tools
search_tool = DuckDuckGoSearchRun()
human_tools = load_tools(["human"])

agent1 = Agent(
    role='Researcher',
    goal="Research then come up with concise answers to questions using the tools that you have access to.",
    verbose=True,
    backstory="You're a researcher that is great at finding information using your tools and providing concise answers to questions.",
    tools=[search_tool],
    allow_delegation=False
)

crew = Crew(
    agents=[agent1],
    tasks=[],
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4-0125-preview")
)

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    crew.tasks=[Task(description=message.content, expected_output="A thorough answer", agent=agent1)]
    response = crew.kickoff()

    await msg.update()

    await cl.Message(
        content=f"{response}",
    ).send()

