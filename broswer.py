from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatGoogleGenerativeAI(api_key=os.environ["GOOGLE_API_KEY"], model="gemini-2.0-flash"),
    )
    await agent.run()

asyncio.run(main())