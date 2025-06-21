from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .tools import hr_tools

class HRAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="alchemyst-special-model", temperature=0)
        self.tools = hr_tools()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You're an HR expert. Answer questions about policies, benefits, and onboarding."),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        self.agent = create_tool_calling_agent(self.llm, self.tools, self.prompt)
        self.executor = AgentExecutor(
            agent=self.agent, 
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True
        )
    
    def run(self, query: str):
        return self.executor.invoke({"input": query})