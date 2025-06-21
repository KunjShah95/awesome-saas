from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

def hr_tools():
    @tool
    def calculate_pto(days: int) -> str:
        """Calculate PTO accrual based on tenure"""
        return f"Accrual: {min(days * 0.5, 20)} days/year"
    
    return [
        DuckDuckGoSearchRun(name="WebSearch"),
        calculate_pto
    ]