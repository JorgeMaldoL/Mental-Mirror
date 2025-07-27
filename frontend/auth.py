import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from auth_service import AuthService

def show_login_page():
    st.title("🪞 Mental Mirror")
    st.markdown("### Welcome! Please sign in to continue your learning journey.")
    
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
                    response = auth_service.sign_in(email, password)
                    if response and response.user:
                        st.session_state.user = response.user
                        st.session_state.authenticated = True
                        st.success("Successfully signed in!")
                        st.rerun()
                    else:
                        st.error("Invalid email or password")
                else:
                    st.error("Please enter both email and password")
    
    with tab2:
        st.subheader("Create Account")
        with st.form("signup_form"):
            new_email = st.text_input("Email", key="signup_email")
            new_password = st.text_input("Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_signup = st.form_submit_button("Create Account")
            
            if submit_signup:
                if new_email and new_password and confirm_password:
                    if new_password == confirm_password:
                        if len(new_password) >= 6:
                            response = auth_service.sign_up(new_email, new_password)
                            if response and response.user:
                                st.success("Account created! Please check your email to verify your account, then sign in.")
                            else:
                                st.error("Account creation failed")
                        else:
                            st.error("Password must be at least 6 characters long")
                    else:
                        st.error("Passwords do not match")
                else:
                    st.error("Please fill in all fields")

def check_authentication():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
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
