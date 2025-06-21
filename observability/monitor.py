import os
from langsmith import Client

def init_observability():
    client = Client()
    print(f"🔭 Observability enabled: https://smith.langchain.com/project/{os.environ['LANGCHAIN_PROJECT']}")

# Call this in your agent initialization