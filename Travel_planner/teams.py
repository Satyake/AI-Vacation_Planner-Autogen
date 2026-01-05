
from autogen_agentchat.teams import RoundRobinGroupChat
from Travel_planner.planner import planner_agent
from Travel_planner.writer import writer_agent
from Travel_planner.researcher import research_agent
from autogen_agentchat.conditions import TextMentionTermination
from Travel_planner.config.settings import TERMINATION_WORD
from Travel_planner.utils.utils import TERMINATION_WORD,save_state,load_state
team=RoundRobinGroupChat(
    participants=[planner_agent,writer_agent,research_agent],
    termination_condition=TextMentionTermination(TERMINATION_WORD)
)
