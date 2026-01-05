
from Travel_planner.config.settings import OPENAI_API_KEY, MODEL, MAX_TURN, MAX_TURN_10, TERMINATION_WORD

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from dotenv import load_dotenv
from autogen_agentchat.ui import Console
import os 
from autogen_agentchat.conditions import TextMentionTermination
from Travel_planner.planner import model_client

#model_client=OpenAIChatCompletionClient(
#    model=MODEL,
#    openai_api_key=OPENAI_API_KEY
#)

research_agent=AssistantAgent(
    name="Researcher",
    description="Your a researcher",
    model_client=model_client,
    system_message="You are a travel researcher, who helps in researching food locations"
)
