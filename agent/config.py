import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AlchemystConfig:
    """Configuration for Alchemyst API integration"""
    
    def __init__(self):
        self.api_key = os.getenv("ALCHEMYST_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY") 
        
        if not self.api_key:
            raise ValueError("ALCHEMYST_API_KEY not found in environment variables")
    
    @property
    def openai_base_url(self):
        """Get the correct OpenAI base URL"""
        # Try Alchemyst proxy first, fallback to direct OpenAI
        return os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    
    @property 
    def effective_api_key(self):
        """Get the effective API key to use"""
        # Use OpenAI key if available, otherwise use Alchemyst key
        return self.openai_api_key or self.api_key
    
    def setup_openai_env(self):
        """Setup OpenAI environment variables"""
        os.environ["OPENAI_API_KEY"] = self.effective_api_key
        os.environ["OPENAI_API_BASE"] = self.openai_base_url
        
        return {
            "api_key": self.effective_api_key,
            "base_url": self.openai_base_url
        }