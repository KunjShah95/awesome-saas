import streamlit as st
import requests

AGENT_ENDPOINTS = {
    "HR Agent": "http://localhost:8000/mcp/agent/hr",
    "Finance Agent": "http://localhost:8000/mcp/agent/finance",
    "IT Agent": "http://localhost:8000/mcp/agent/it",
}

st.title("🤖 Multi-Agent Portal")
st.caption("Powered by Alchemyst AI")

agent_choice = st.selectbox("Choose an agent:", list(AGENT_ENDPOINTS.keys()))
question = st.text_input(f"Ask {agent_choice} questions:")

if st.button("Submit") and question:
    with st.spinner(f"Consulting {agent_choice}..."):
        response = requests.post(
            AGENT_ENDPOINTS[agent_choice], json={"input": question}
        )
        if response.status_code == 200:
            st.success(response.json()["output"])
        else:
            st.error("Agent failed to respond")

st.divider()
st.subheader("Observability Dashboard")
st.write("""
- [LangSmith Traces](https://smith.langchain.com)
- [Agent Metrics](#)  # Add your observability link
""")
