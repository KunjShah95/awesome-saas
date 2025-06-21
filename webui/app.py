import streamlit as st
import requests

# MCP Server endpoint
MCP_URL = "http://localhost:8000/mcp/agent"

st.title("🤖 HR Agent Portal")
st.caption("Powered by Alchemyst AI")

question = st.text_input("Ask HR questions:")
if st.button("Submit") and question:
    with st.spinner("Consulting HR policies..."):
        response = requests.post(MCP_URL, json={"input": question})
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