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
  description='Tell me about data engineering',
  expected_output='A bulleted list of the top 5 most important aspects of the topic',
  agent=basic_agent
)

crew = Crew(
    agents=[basic_agent],
    tasks=[task],
    verbose=1
)

result = crew.kickoff()
print(result)