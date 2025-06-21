import os

os.environ["LANGCHAIN_TRACING_V2"] = "false"

from fastapi import FastAPI
from pydantic import BaseModel
from agent.hr_agent import HRAgent
from agent.finance_agent import FinanceAgent
from agent.it_agent import ITAgent
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="HR Agent MCP Server")
hr_agent = HRAgent()
finance_agent = FinanceAgent()
it_agent = ITAgent()


class AgentRequest(BaseModel):
    input: str


@app.post("/mcp/agent/hr")
async def run_hr_agent(request: AgentRequest):
    result = hr_agent.run(request.input)
    return {"output": result["output"]}


@app.post("/mcp/agent/finance")
async def run_finance_agent(request: AgentRequest):
    result = finance_agent.run(request.input)
    return {"output": result["output"]}


@app.post("/mcp/agent/it")
async def run_it_agent(request: AgentRequest):
    result = it_agent.run(request.input)
    return {"output": result["output"]}


@app.get("/")
def root():
    return {"message": "Welcome to the HR Agent MCP Server!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
