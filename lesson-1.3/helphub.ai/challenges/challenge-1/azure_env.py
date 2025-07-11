import os
from dotenv import load_dotenv

def load_azure_openai_env():
    """
    Loads Azure OpenAI environment variables from .env file.
    Returns a dictionary with API key, endpoint, API version, and deployment name.
    """
    load_dotenv()
    return {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
        "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    }