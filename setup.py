#!/usr/bin/env python3
"""
Setup script for Awesome SaaS App
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False
    return True

def check_env_file():
    """Check if .env file is properly configured"""
    print("🔍 Checking environment configuration...")
    
    if not os.path.exists(".env"):
        print("❌ .env file not found!")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
    
    if "your-openai-api-key-here" in content:
        print("⚠️  Please update your .env file with a valid OpenAI API key")
        print("   Get your API key from: https://platform.openai.com/api-keys")
        return False
    
    print("✅ Environment configuration looks good!")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Awesome SaaS App...")
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check environment
    env_ok = check_env_file()
    
    print("\n" + "="*50)
    print("📋 Setup Summary:")
    print("="*50)
    print("✅ Dependencies installed")
    
    if env_ok:
        print("✅ Environment configured")
        print("\n🎉 Setup complete! You can now run:")
        print("   python -m uvicorn server.main:app --reload")
        print("   streamlit run webui/app.py")
    else:
        print("⚠️  Environment needs configuration")
        print("\n📝 Next steps:")
        print("1. Update .env file with your OpenAI API key")
        print("2. Run: python -m uvicorn server.main:app --reload")
        print("3. Run: streamlit run webui/app.py")

if __name__ == "__main__":
    main()