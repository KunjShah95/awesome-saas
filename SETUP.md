# 🚀 Setup Guide for Awesome SaaS App

## Prerequisites
- Python 3.8+
- OpenAI API key (get from [OpenAI Platform](https://platform.openai.com/api-keys))

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/KunjShah95/awesome-saas.git
cd awesome-saas
```

### 2. Run the setup script
```bash
python setup.py
```

### 3. Configure your API keys
- Edit `.env` file
- Replace `your-openai-api-key-here` with your actual OpenAI API key

### 4. Start the application
```bash
# Terminal 1: Start the API server
python -m uvicorn server.main:app --reload

# Terminal 2: Start the web UI
streamlit run webui/app.py
```

### 5. Access the application
- Web UI: http://localhost:8501
- API Docs: http://localhost:8000/docs

## 🤖 Available Agents

- **HR Agent**: Handles HR policies, benefits, and onboarding questions
- **Finance Agent**: Manages budgets, expenses, and reimbursements  
- **IT Agent**: Provides technical support and troubleshooting

## 🔧 Troubleshooting

### Common Issues

#### 1. API Key Issues
```
OpenAI API error: Incorrect API key provided
```
**Solution**: Update your `.env` file with a valid OpenAI API key

#### 2. Module Import Errors
```
ModuleNotFoundError: No module named 'langchain'
```
**Solution**: Run `pip install -r requirements.txt`

#### 3. Port Already in Use
```
OSError: [Errno 48] Address already in use
```
**Solution**: Use different ports:
```bash
uvicorn server.main:app --port 8001
streamlit run webui/app.py --server.port 8502
```

#### 4. Alchemyst API Connectivity
If Alchemyst proxy is unavailable, the app automatically falls back to direct OpenAI API calls.

### Manual Installation

If the setup script fails, install manually:
```bash
pip install fastapi uvicorn streamlit langchain langchain-openai
pip install langchain-community python-dotenv requests openai
pip install pydantic duckduckgo-search
```

## 🔑 API Configuration

The app supports multiple API configurations:

1. **Alchemyst API** (primary): Uses your Alchemyst API key
2. **OpenAI API** (fallback): Direct OpenAI API calls

The configuration automatically detects which API to use based on availability.

## 📝 Environment Variables

```bash
# Alchemyst API Configuration
ALCHEMYST_API_KEY=your-alchemyst-key

# OpenAI API Configuration (fallback)
OPENAI_API_KEY=your-openai-key
OPENAI_BASE_URL=https://api.openai.com/v1
```

## 🧪 Testing

Test individual agents:
```bash
# Test HR Agent
curl -X POST "http://localhost:8000/mcp/agent/hr" \
     -H "Content-Type: application/json" \
     -d '{"input": "What is the PTO policy?"}'

# Test Finance Agent  
curl -X POST "http://localhost:8000/mcp/agent/finance" \
     -H "Content-Type: application/json" \
     -d '{"input": "Calculate budget for $10000"}'

# Test IT Agent
curl -X POST "http://localhost:8000/mcp/agent/it" \
     -H "Content-Type: application/json" \
     -d '{"input": "Reset password for user john"}'
```

## 🐛 Debug Mode

Enable verbose logging:
```bash
export LANGCHAIN_VERBOSE=true
python -m uvicorn server.main:app --reload --log-level debug
```

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your API keys are correct
3. Ensure all dependencies are installed
4. Check the console logs for detailed error messages