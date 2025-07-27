import os
from dotenv import load_dotenv
from pathlib import Path

project_root = Path(__file__).parent.parent
env_path = project_root / '.env'
load_dotenv(env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def validate_config():
    if not OPENAI_API_KEY:
        raise ValueError(f"OPENAI_API_KEY is required in environment variables. Looking for .env at: {env_path}")
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY are required for database functionality")
    return True
