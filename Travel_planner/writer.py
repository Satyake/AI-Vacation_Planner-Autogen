
from Travel_planner.config.settings import OPENAI_API_KEY, MODEL, MAX_TURN, MAX_TURN_10, TERMINATION_WORD

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from autogen_agentchat.conditions import TextMentionTermination
from Travel_planner.planner import model_client

# model_client is shared from planner to keep configuration consistent

writer_agent = AssistantAgent(
    name="Writer",
    description="You are a travel writer",
    model_client=model_client,
    system_message=(
        "You are a travel writer. Your job is to take research findings and plans "
        "and convert them into clear, engaging, and well-structured travel content. "
        "Write concise itineraries, descriptions of places, food experiences, and tips "
        "in a friendly, professional tone."
    )
)
