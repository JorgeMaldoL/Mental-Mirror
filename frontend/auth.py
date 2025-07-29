import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from auth_service import AuthService

def show_login_page():
    st.title("🪞 Mental Mirror")
    st.markdown("### Welcome! Please sign in to continue your learning journey.")
    
    with st.expander("ℹ️ New user? Read this first"):
        st.markdown("""
        **How to get started:**
        1. **Sign Up** with a **valid email address**
        2. **Check your email** for a confirmation link
        3. **Click the confirmation link** - you'll be automatically signed in
        4. Start using Mental Mirror! 🎉
        
        **Note:** You must verify your email before you can sign in.
        """)
    
    auth_service = AuthService()
    
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        st.subheader("Sign In")
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit_login = st.form_submit_button("Sign In")
            
            if submit_login:
                if email and password:
                    if "@" not in email or "." not in email:
                        st.error("❌ Please enter a valid email address.")
                    else:
                        response = auth_service.sign_in(email, password)
                        if response and response.user:
                            st.session_state.user = response.user
                            st.session_state.authenticated = True
                            st.success("✅ Successfully signed in!")
                            st.rerun()
                else:
                    st.error("❌ Please enter both email and password")
    
    with tab2:
        st.subheader("Create Account")
        with st.form("signup_form"):
            new_email = st.text_input("Email", key="signup_email")
            new_password = st.text_input("Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_signup = st.form_submit_button("Create Account")
            
            if submit_signup:
                if new_email and new_password and confirm_password:
                    if "@" not in new_email or "." not in new_email:
                        st.error("❌ Please enter a valid email address.")
                    elif new_password == confirm_password:
                        if len(new_password) >= 6:
                            response = auth_service.sign_up(new_email, new_password)
                            if response and response.user:
                                st.success("✅ Account created! Please check your email and click the confirmation link to activate your account. You'll be automatically signed in after confirmation.")
                            else:
                                st.error("❌ Account creation failed. Please try again.")
                        else:
                            st.error("❌ Password must be at least 6 characters long")
                    else:
                        st.error("❌ Passwords do not match")
                else:
                    st.error("❌ Please fill in all fields")

def check_authentication():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    # Check for email confirmation in URL parameters
    query_params = st.query_params
    if 'access_token' in query_params and 'refresh_token' in query_params:
        try:
            auth_service = AuthService()
            access_token = query_params['access_token']
            refresh_token = query_params['refresh_token']
            
            # Set the session with the tokens from email confirmation
            auth_service.supabase.auth.set_session(access_token, refresh_token)
            
            # Store in session state
            st.session_state.access_token = access_token
            st.session_state.refresh_token = refresh_token
            st.session_state.authenticated = True
            
            # Get user info
            user = auth_service.get_current_user()
            if user:
                st.session_state.user = user
                st.success("Email confirmed! Welcome to Mental Mirror!")
                # Clear the URL parameters
                st.query_params.clear()
                st.rerun()
        except Exception as e:
            st.error(f"Email confirmation failed: {str(e)}")
    
    if not st.session_state.authenticated:
        auth_service = AuthService()
        user = auth_service.get_current_user()
        if user:
            st.session_state.user = user
            st.session_state.authenticated = True
        else:
            show_login_page()
            st.stop()
    
    return True

def show_logout_button():
    auth_service = AuthService()
    with st.sidebar:
        st.write(f"Welcome, {st.session_state.user.email}")
        if st.button("Sign Out"):
            auth_service.sign_out()
            st.session_state.authenticated = False
            st.rerun()
