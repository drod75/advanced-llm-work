import asyncio
from crawl4ai import AsyncWebCrawler

# Setting up langchain link
langchain_url = 'https://python.langchain.com/api_reference/'

# Using AsyncWebCrawler
async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=langchain_url)
        print(result.markdown[:300])  # Print first 300 chars

if __name__ == "__main__":
    asyncio.run(main())