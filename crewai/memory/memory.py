import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

basic_agent = Agent(
    role='A helpful assistant',
    goal='Answer questions',
    backstory="""You're an assistant that is intelligent and helpful.""",
    verbose=True
)

task = Task(
  description='What is my name?',
  expected_output='Information',
  agent=basic_agent
)

crew = Crew(
    agents=[basic_agent],
    tasks=[task],
    memory=True,
    verbose=1
)

result = crew.kickoff()
print(result)