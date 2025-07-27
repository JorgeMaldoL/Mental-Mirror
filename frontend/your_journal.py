import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from prompt_templates import JournalAI
from supabase_service import SupabaseService
from auth_service import AuthService
from auth import check_authentication

# Ensure user is authenticated
check_authentication()

st.title("📝 Your Journal")
st.markdown("This is simply your daily journal. Talk about your day and explain ideas that you have. You can also press the 'Explain to AI' Button and this will trigger the AI to respond to your text with clarifying questions and advice.")

st.markdown("**:green[What was your day like?] " + "&nbsp;" + ":green[What's on your mind?] " + "&nbsp;" + ":green[Do you have an idea that you'd like to write out?]**")

if 'journal_ai' not in st.session_state:
    st.session_state.journal_ai = JournalAI()

if 'supabase_service' not in st.session_state:
    st.session_state.supabase_service = SupabaseService()

journal_text = st.text_area("Journal Entry", height=300, placeholder="Start writing about your day, thoughts, or ideas...", label_visibility="collapsed")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Save Entry", type="primary"):
        if journal_text:
            user_id = st.session_state.user.id
            success = st.session_state.supabase_service.save_journal_entry(
                user_id=user_id,
                content=journal_text
            )
            if success:
                st.success("Entry saved to your journal!")
                st.rerun()
            else:
                st.error("Failed to save entry. Please try again.")
        else:
            st.warning("Please write something before saving.")

with col2:
    if st.button("Explain to AI"):
        if journal_text:
            with st.spinner("🤖 AI is analyzing your journal entry..."):
                try:
                    ai_response = st.session_state.journal_ai.analyze_entry(journal_text)
                    
                    if ai_response:
                        st.markdown("### 🤖 AI Analysis")
                        st.markdown(ai_response)
                        
                        # Save with AI response
                        user_id = st.session_state.user.id
                        st.session_state.supabase_service.save_journal_entry(
                            user_id=user_id,
                            content=journal_text,
                            ai_response=ai_response
                        )
                    else:
                        st.error("Sorry, I couldn't analyze your entry right now. Please try again.")
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.info("Please check your API key in the .env file.")
        else:
            st.warning("Please write something for the AI to analyze.")

st.markdown("---")
st.subheader("📚 Your Previous Entries")

# Load and display previous entries
user_id = st.session_state.user.id
entries = st.session_state.supabase_service.get_journal_entries(user_id)

if entries:
    for entry in entries:
        with st.expander(f"Entry from {entry['created_at'][:10]}"):
            st.write(entry['content'])
            if entry['ai_response']:
                st.markdown("**🤖 AI Analysis:**")
                st.markdown(entry['ai_response'])
else:
    st.info("No previous entries found. Start writing to build your journal history!")
