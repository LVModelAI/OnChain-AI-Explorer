import pytest
from aioresponses import aioresponses  
from dotenv import load_dotenv
import os
import asyncio
import web3ai  #this is the library i made

load_dotenv()
EXPLORER_BASE_URL = os.getenv("EXPLORER_BASE_URL")
EXPLORER_API_KEY = os.getenv("EXPLORER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def main():
    prompt = input("Enter prompt: ")

    func_result = await web3ai.execute_function_from_prompt(EXPLORER_BASE_URL, EXPLORER_API_KEY, OPENAI_API_KEY, prompt)

    print(f"Function result: {func_result}")

asyncio.run(main())
