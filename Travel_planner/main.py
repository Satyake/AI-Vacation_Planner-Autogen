from autogen_agentchat.messages import TextMessage
from Travel_planner.teams import team
import asyncio
async def main():
    result= await team.run(task=TextMessage(content="Plan a trip to India for 5 days", source="user"))
    print(result.messages[-1].content)

#if __name__=="__main__":
#    asyncio.run(main())
