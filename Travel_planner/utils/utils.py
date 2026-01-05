from autogen_agentchat.conditions import TextMentionTermination
import json
from Travel_planner.config.settings import TERMINATION_WORD
text_mention_termination=TextMentionTermination(TERMINATION_WORD)

def save_state(agent, file_name):
    state=agent.save_state()
    with open(file_name,'w') as f:
        json.dump(state,f)


def load_state(agent, file_name):
    state=agent.save_state()
    with open(file_name,'r') as f:
        state=json.load(f)
    agent.load_state(state)