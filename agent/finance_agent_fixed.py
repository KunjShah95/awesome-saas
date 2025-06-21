import os
from dotenv import load_dotenv
import requests
import openai
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .tools import finance_tools
from .config import AlchemystConfig

# Load environment variables
load_dotenv()

class FinanceAgent:
    def __init__(self):
        try:
            # Initialize configuration
            self.config = AlchemystConfig()
            config_info = self.config.setup_openai_env()
            
            # Test API connectivity
            self._test_api_connectivity()
            
            # Initialize LLM with configuration
            self.llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                temperature=0,
                openai_api_key=config_info["api_key"],
                openai_api_base=config_info["base_url"]
            )
            
            self.tools = finance_tools()
            self.prompt = ChatPromptTemplate.from_messages([
                (
                    "system",
                    "You're a Finance expert. Answer questions about budgets, expenses, and reimbursements.",
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ])
            
            self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
            self.executor = AgentExecutor(
                agent=self.agent, tools=self.tools, verbose=True, handle_parsing_errors=True
            )
            
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Finance Agent: {str(e)}")

    def _test_api_connectivity(self):
        """Test API connectivity with fallback options"""
        try:
            # Test OpenAI API directly
            client = openai.OpenAI(
                api_key=self.config.effective_api_key,
                base_url=self.config.openai_base_url
            )
            # Simple test call
            client.models.list()
            print(f"✅ API connectivity successful using: {self.config.openai_base_url}")
        except Exception as e:
            print(f"⚠️ API connectivity issue: {str(e)}")
            print("Please check your API keys and network connection")

    def run(self, query: str):
        """Execute a query using the finance agent"""
        try:
            return self.executor.invoke({"input": query})
        except openai.OpenAIError as e:
            return {"output": f"OpenAI API error: {str(e)}"}
        except Exception as e:
            return {"output": f"Agent error: {str(e)}"}