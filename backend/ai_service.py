from openai import OpenAI
from typing import Optional
from config import OPENAI_API_KEY, AI_MODEL, validate_config

class AIService:
    def __init__(self):
        validate_config()
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = AI_MODEL

    def get_response(self, prompt: str, max_tokens: int = 500) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.8
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return None
        
    def get_record()