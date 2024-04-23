import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

research_agent = Agent(
    role='AI Agent Researcher',
    goal='Find and summarize the latest AI Agent news',
    backstory="""You're an AI agent researcher at a leading university.
    You're responsible for analyzing data and providing insights
    to the department and your students.""",
    verbose=True
)

task = Task(
  description='Find and summarize the latest AI agent news',
  expected_output='A bullet list summary of the top 5 most important AI agent news items',
  agent=research_agent
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()
print(result)