from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool


def hr_tools():
    @tool
    def calculate_pto(days: int) -> str:
        """Calculate PTO accrual based on tenure"""
        return f"Accrual: {min(days * 0.5, 20)} days/year"

    return [DuckDuckGoSearchRun(name="WebSearch"), calculate_pto]


def finance_tools():
    @tool
    def calculate_budget(amount: float) -> str:
        """Calculate remaining budget after expenses"""
        return f"Remaining budget: ${amount * 0.8:.2f} (assumes 20% spent)"

    return [DuckDuckGoSearchRun(name="WebSearch"), calculate_budget]


def it_tools():
    @tool
    def reset_password(username: str) -> str:
        """Reset a user's password"""
        return f"Password for {username} has been reset."

    return [DuckDuckGoSearchRun(name="WebSearch"), reset_password]
