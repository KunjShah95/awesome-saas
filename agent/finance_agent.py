import os
from dotenv import load_dotenv

# Load environment variables from .env file as early as possible
load_dotenv()

alchemyst_api_key = os.getenv("ALCHEMYST_API_KEY")
if not alchemyst_api_key:
    raise RuntimeError(
        "ALCHEMYST_API_KEY is not set in your .env file. Please add it and restart."
    )
os.environ["OPENAI_API_KEY"] = alchemyst_api_key
os.environ["OPENAI_API_BASE"] = (
    "https://alchemyst-ai.com/api/v1/proxy/https://api.openai.com/v1/"
)

import requests

# Check connectivity to Alchemyst proxy endpoint
try:
    resp = requests.get("https://alchemyst-ai.com/api/v1/")
    if resp.status_code >= 400:
        raise RuntimeError(
            "Cannot reach Alchemyst proxy endpoint. Status code: {}".format(
                resp.status_code
            )
        )
except Exception as e:
    raise RuntimeError(f"Failed to connect to Alchemyst proxy endpoint: {e}")

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .tools import finance_tools
import openai


class FinanceAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.tools = finance_tools()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You're a Finance expert. Answer questions about budgets, expenses, and reimbursements.",
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.executor = AgentExecutor(
            agent=self.agent, tools=self.tools, verbose=True, handle_parsing_errors=True
        )

    def run(self, query: str):
        try:
            return self.executor.invoke({"input": query})
        except openai.OpenAIError as e:
            return {"output": f"OpenAI API error: {str(e)}"}
        except Exception as e:
            return {"output": f"Agent error: {str(e)}"}
