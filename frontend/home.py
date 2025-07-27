import streamlit as st

st.set_page_config(page_title="Mental Mirror", page_icon="🧠", layout="wide")

st.sidebar.title("Mental Mirror")

# Welcome message
st.title("🧠 Welcome to Mental Mirror")
st.markdown("Your personal AI-powered learning and reflection companion.")
st.markdown("Choose a mode from the navigation to get started:")


Your_Journal = st.Page(
    "your_journal.py",
    title="Your Journal", 
    icon="📝",
)

Feynman_Mode = st.Page(
    "feynman_mode.py",
    title="Feynman mode", 
    icon="🏫",
)

Speech_Practice = st.Page(
    "speech_practice.py",
    title="Speech Practice", 
    icon= "🗣️",
)

Summarize_Training = st.Page(
    "summarize_training.py",
    title="Summarize Training", 
    icon="🎯"
)

pg = st.navigation([Your_Journal, Feynman_Mode, Speech_Practice, Summarize_Training])
pg.run()
