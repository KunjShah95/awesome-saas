from fastapi import FastAPI
from pydantic import BaseModel
from agent.hr_agent import HRAgent
import uvicorn


app = FastAPI(title="HR Agent MCP Server")
agent = HRAgent()


class AgentRequest(BaseModel):
    input: str


@app.post("/mcp/agent")
async def run_agent(request: AgentRequest):
    result = agent.run(request.input)
    return {"output": result["output"]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
