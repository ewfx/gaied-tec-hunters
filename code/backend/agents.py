from crewai import Agent
from textwrap import dedent
# from langchain_google_genai import ChatGoogleGenerativeAI
import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Given an api and required clear doc about the endpoints of the api and also the acceptance criteria of the test case
the agent should give the feature and the step definition file which is needed in maven project

Captain/Manager/Boss:
-  testAI

Employees/Experts to hire:
-none



Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class TestAgents:
    def __init__(self):
        # Declaring the llm
        model = "sambanova/DeepSeek-R1-Distill-Llama-70B"
        self.llm = LLM(
            model=model,
            base_url=os.getenv("SAMBANOVA_BASE_URL"),
            api_key=os.getenv("SAMBANOVA_API_KEY")
        )

    def email_data_extractor(self):
        return Agent(
            role = dedent(f"""Financial Email analysis expert."""),

            backstory = dedent(f""" Commercial Bank Lending Service teams receive a significant volume of servicing requests 
            through emails. These emails contain diverse requests, often with attachments and will be ingested to the 
            loan servicing platform and creates service requests which will go through the workflow processing.
            You are a very experienced and expert financial email analyser who has done this job for a long time 
            perfectly for the company"""),

            goal = dedent(f""" Your goal is to extract all the information provided in the mail according to the context
             of the mail and populate the fields of a given template """),

            llm=self.llm
        )






























# class TestAgents:
#     def __init__(self):
#         # Declaring the llm
#         model = "DeepSeek-R1-Distill-Llama-70B"
#         self.llm = LLM(
#             model=model,
#             base_url=os.getenv("SAMBANOVA_BASE_URL"),
#             api_key=os.getenv("SAMBANOVA_API_KEY")
#         )
#
#     def feature_generator(self):
#         return Agent(
#             role=dedent(f"""Gherkin feature file generator expert"""),
#
#             backstory=dedent(f"""You are an expert in gherkin language with full knowledge about the syntax of the gherkin language
#                             and has worked in many projects to convert given english criteria to a gherkin test case content of feature file
#                             required for testing an api using cucumber bdd framework in java maven project  """),
#
#             goal=dedent(f"""
#                         provide the content of the feature file for the given documentation of the api
#                         and the acceptance criteria for the test case"""),
#             verbose=True,
#             max_iter=25,
#             llm=self.genai,
#         )
#
#     def step_def_generator(self):
#         return Agent(
#             role=dedent(f"""Expert Java maven step definition file generator"""),
#
#             backstory=dedent(f"""You are an expert in producing the content of step definition file in java language when the feature
#                             file(gherkin language) is given  """),
#             goal=dedent(f"""
#                         provide the content of the stepdefinition file in java language accurately with no syntax error"""),
#             verbose=True,
#             max_iter=20,
#             llm=self.genai,
#         )
#
#     def pom_file_generator(self):
#         return Agent(
#             role=dedent(f"""Expert Java maven pom.xml file generator"""),
#
#             backstory=dedent(f"""You are an expert in producing the content of pom.xml file in java language for the given stepdefinition file
#                             to solve all the dependency issues and you have never missed out to add any dependency in pom.xml file which is
#                             needed to run the stepdefinition file"""),
#             goal=dedent(f"""
#                         provide the content of the pom.xml file to resolve all dependencies for the given stepdefinition file"""),
#             verbose=True,
#             max_iter=20,
#             llm=self.genai,
#         )






