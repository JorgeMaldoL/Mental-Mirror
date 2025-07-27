import streamlit as st
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

class AuthService:
    def __init__(self):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    def sign_up(self, email: str, password: str):
        try:
            response = self.supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            return response
        except Exception as e:
            st.error(f"Sign up failed: {str(e)}")
            return None
    
    def sign_in(self, email: str, password: str):
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            if response.user and response.session:
                # Set the session in the client for RLS to work
                self.supabase.auth.set_session(response.session.access_token, response.session.refresh_token)
                # Store session info in streamlit session state
                import streamlit as st
                st.session_state.access_token = response.session.access_token
                st.session_state.refresh_token = response.session.refresh_token
            return response
        except Exception as e:
            st.error(f"Sign in failed: {str(e)}")
            return None
    
    def sign_out(self):
        try:
            self.supabase.auth.sign_out()
            st.session_state.clear()
        except Exception as e:
            st.error(f"Sign out failed: {str(e)}")
    
    def get_current_user(self):
        try:
            user = self.supabase.auth.get_user()
            return user.user if user else None
        except:
            return None
    
    def is_authenticated(self):
        return self.get_current_user() is not None
