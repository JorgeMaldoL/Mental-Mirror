from supabase import create_client, Client
from datetime import datetime
from typing import List, Dict
from config import SUPABASE_URL, SUPABASE_KEY
import streamlit as st

class SupabaseService:
    def __init__(self, auth_service=None):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Set the session if we have tokens stored
        if hasattr(st.session_state, 'access_token') and hasattr(st.session_state, 'refresh_token'):
            try:
                self.client.auth.set_session(st.session_state.access_token, st.session_state.refresh_token)
            except:
                pass  # If tokens are invalid, continue without auth
    
    def save_journal_entry(self, user_id: str, content: str, ai_response: str = None) -> bool:
        try:
            entry_data = {
                "user_id": user_id,
                "content": content,
                "ai_response": ai_response
            }
            self.client.table("journal_entries").insert(entry_data).execute()
            return True
        except Exception as e:
            print(f"Error saving journal entry: {e}")
            return False
    
    def get_journal_entries(self, user_id: str, limit: int = 10) -> List[Dict]:
        try:
            result = self.client.table("journal_entries")\
                .select("*")\
                .eq("user_id", user_id)\
                .order("created_at", desc=True)\
                .limit(limit)\
                .execute()
            return result.data
        except Exception as e:
            print(f"Error fetching journal entries: {e}")
            return []
    
    def save_feynman_session(self, user_id: str, topic: str, explanation: str, ai_feedback: str = None) -> bool:
        try:
            session_data = {
                "user_id": user_id,
                "topic": topic,
                "explanation": explanation,
                "ai_feedback": ai_feedback
            }
            self.client.table("feynman_sessions").insert(session_data).execute()
            return True
        except Exception as e:
            print(f"Error saving Feynman session: {e}")
            return False
    
    def get_feynman_entries(self, user_id: str, limit: int = 10) -> List[Dict]:
        try:
            result = self.client.table("feynman_sessions")\
                .select("*")\
                .eq("user_id", user_id)\
                .order("created_at", desc=True)\
                .limit(limit)\
                .execute()
            return result.data
        except Exception as e:
            print(f"Error fetching Feynman entries: {e}")
            return []
    
    def save_speech_session(self, user_id: str, practice_type: str, prompt: str, 
                           confidence: int, clarity: int, notes: str = None) -> bool:
        try:
            session_data = {
                "user_id": user_id,
                "practice_type": practice_type,
                "prompt": prompt,
                "confidence_rating": confidence,
                "clarity_rating": clarity,
                "notes": notes
            }
            self.client.table("speech_sessions").insert(session_data).execute()
            return True
        except Exception as e:
            print(f"Error saving speech session: {e}")
            return False
    
    def save_summary_session(self, user_id: str, original_text: str, user_summary: str, 
                            summary_type: str, audience: str, ai_feedback: str = None) -> bool:
        try:
            session_data = {
                "user_id": user_id,
                "original_text": original_text,
                "user_summary": user_summary,
                "summary_type": summary_type,
                "audience": audience,
                "ai_feedback": ai_feedback
            }
            self.client.table("summary_sessions").insert(session_data).execute()
            return True
        except Exception as e:
            print(f"Error saving summary session: {e}")
            return False
