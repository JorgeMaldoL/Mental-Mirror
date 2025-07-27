import streamlit as st
from auth import check_authentication, show_logout_button

st.set_page_config(page_title="Mental Mirror", page_icon="🧠", layout="wide")

# Check authentication first
check_authentication()

st.sidebar.title("Mental Mirror")
show_logout_button()

st.title("🧠 Welcome to Mental Mirror")
st.markdown("Your personal AI-powered learning and reflection companion. Choose a mode from the navigation to get started:")

Your_Journal = st.Page("your_journal.py", title="Your Journal", icon="📝")
Feynman_Mode = st.Page("feynman_mode.py", title="Feynman mode", icon="🏫")
Speech_Practice = st.Page("speech_practice.py", title="Speech Practice", icon="🗣️")
Summarize_Training = st.Page("summarize_training.py", title="Summarize Training", icon="🎯")

pg = st.navigation([Your_Journal, Feynman_Mode, Speech_Practice, Summarize_Training])
pg.run()
