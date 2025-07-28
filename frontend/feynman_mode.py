import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from prompt_templates import FeynmanAI
from supabase_service import SupabaseService
from auth_service import AuthService
from auth import check_authentication

check_authentication()

st.title("🏫 Feynman Mode")
st.markdown("**The Feynman Technique**: Explain complex concepts in simple terms as if teaching someone else.")
st.markdown("""
1. **Choose a concept** you want to understand
2. **Explain it simply** as if teaching a child
3. **Identify gaps** where your explanation breaks down
4. **Go back and study** those specific areas
5. **Repeat** until you can explain it clearly
""")
st.info("💡 **Tip**: If you can't explain it simply, you don't understand it well enough!")
st.markdown("---")

if 'feynman_ai' not in st.session_state:
    st.session_state.feynman_ai = FeynmanAI()

if 'supabase_service' not in st.session_state:
    st.session_state.supabase_service = SupabaseService()

topic = st.text_input("What topic would you like to explain?", placeholder="e.g., Quantum Physics, Machine Learning, Economics...")

if topic:
    st.markdown(f"**Explain '{topic}' as if teaching it to someone who knows nothing about it:**")
    
    explanation = st.text_area(
        "Your explanation:",
        height=300, 
        placeholder="Start with the basics and build up your explanation. Use simple language and analogies...",
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Get AI Feedback", type="primary"):
            if explanation:
                with st.spinner("🤖 AI is creating feedback..."):
                    try:
                        ai_response = st.session_state.feynman_ai.evaluate_explanation(topic, explanation)
                        if ai_response:
                            st.markdown("### 🤖 AI Feedback")
                            st.markdown(ai_response)

                            user_id = st.session_state.user.id
                            st.session_state.supabase_service.save_feynman_session(
                                user_id=user_id,
                                topic=topic, 
                                explanation= explanation,
                                ai_feedback= ai_response
                            )
                        else:
                            st.warning("Sorry, I can't give you feedback right now. Please try again later.")
                    except Exception as e:
                        st.error(f"An error occured: {str(e)}")
                        st.info("Please check the api key for .env file")
            else:
                st.warning("Please write an explaination for the AI to give feedback on.")
    
    with col2:
        if st.button("Save Explanation"):
            if explanation:
                user_id = st.session_state.user.id
                success = st.session_state.supabase_service.save_feynman_session(
                    user_id=user_id,
                    topic=topic,
                    explanation=explanation,
                    ai_feedback=None
                )
                if success:
                    st.success("Explanation saved!")
                else:
                    st.error("Failed to save explanation. Please try again.")
            else:
                st.warning("Please write something before saving.")

user_id = st.session_state.user.id
entries = st.session_state.supabase_service.get_feynman_entries(user_id)

if entries:
    st.markdown("### 📝 Previous Explanations")
    for entry in entries:
        with st.expander(f"📚 {entry['topic']} - {entry['created_at'][:10]}"):
            st.markdown("**Your Explanation:**")
            st.write(entry['explanation'])
            if entry['ai_feedback']:
                st.markdown("**🤖 AI Feedback:**")
                st.markdown(entry['ai_feedback'])
else:
    st.info("No previous entries found. Start explaining a concept above!")
