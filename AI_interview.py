
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from dotenv import load_dotenv
from autogen_agentchat.ui import Console
import os 
from autogen_agentchat.conditions import TextMentionTermination

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
model_client=OpenAIChatCompletionClient(model="gpt-4o")
job_position="software engineer"
#Interviewer
interviewer=AssistantAgent(
    name="interviewer",
    model_client=model_client,
    system_message=f"""
    You are a professional interviewer for a{job_position}.

    Ask one clear question at a time and wait for the user to respond.
    Ask 3 questions in total covering technical skills and experience.
    Dont pay attention to Career coach responses, Make sure to ask questions based on candidates expertise.
    After asking 3 questions, say, 'TERMINATE' at the end of the interview.
    """
)

#Interviewee Agent # userproxyagent #user feedback
interviewee=UserProxyAgent(
    name="Interviewee",
    description="for input ",
    input_func=input,
)

#career coach
career_coach=AssistantAgent(
    name="careercoach",
    model_client=model_client,
    system_message=f"""
   you are a career coach specialized in preparing candidates for {job_position} interviews,
   after the interview provide summarized feedback under 100 words"""
)

team=RoundRobinGroupChat(
    [interviewer,interviewee,career_coach],
    max_turns=20,
    termination_condition=TextMentionTermination(text="TERMINATE")
)


async def main():
    await Console(team.run_stream(task="Conduct an interview for a software engineering position"))
#running the agent team
import asyncio
if __name__=="__main__":

    asyncio.run(main())
