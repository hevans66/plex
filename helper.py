import argparse
import os
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import tool
import os
import re
from typing import List
from langchain.agents import initialize_agent, Tool
from langchain.tools import BaseTool
from langchain.llms import OpenAI

class PlexJobs(BaseTool):
    name = "plex jobs"
    description = "useful for when you need to use PLEX or run computational biology applications"

    def _run(self, query: str) -> str:
        """Searches PLEX for jobs that have run in the past"""
        # uuid_pattern = re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
        # matching_dirs = []

        # for entry in os.scandir():
        #     if entry.is_dir() and uuid_pattern.fullmatch(entry.name):
        #         if query.lower() in entry.name.lower():
        #             matching_dirs.append(entry.name)
        # return matching_dirs
        return os.listdir()
    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Plex does not support async")


def main(args):
    # Load environment variables from .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")
    wolfram_app_id = os.getenv("WOLFRAM_APP_ID")
    #wolfram_app_id = os.getenv("SERPAPI_API_KEY")

    # First, let's load the language model we're going to use to control the agent.
    llm = OpenAI(temperature=0)

    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    #tools = [PlexJobs()]
    tools = load_tools(["terminal"], llm=llm)
    #tools = load_tools(["terminal", "serpapi", "wolfram-alpha", "llm-math"], llm=llm)

    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

    # Now let's test it out!
    result = agent.run(args.query)
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run langchain-based queries.")
    parser.add_argument("query", type=str, help="The query to run through the langchain agent.")
    args = parser.parse_args()
    main(args)
