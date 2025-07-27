import streamlit as st
import datetime

st.title("🗣️ Speech Practice")
st.markdown("Practice your speaking skills, whether it's for presentations, interviews, or general communication improvement.")

# Practice type selection
practice_type = st.selectbox(
    "What would you like to practice?",
    ["Public Speaking", "Interview Preparation", "Presentation Skills", "Conversation Practice", "Debate/Argumentation"]
)

if practice_type:
    st.markdown(f"**Practicing: {practice_type}**")
    
    # Topic or prompt
    if practice_type == "Interview Preparation":
        prompt = st.selectbox(
            "Choose an interview question:",
            [
                "Tell me about yourself",
                "What are your strengths and weaknesses?",
                "Why do you want this job?",
                "Describe a challenging situation you faced",
                "Where do you see yourself in 5 years?"
            ]
        )
    elif practice_type == "Public Speaking":
        prompt = st.text_input("Enter your speech topic:", placeholder="e.g., Climate Change, Technology in Education...")
    else:
        prompt = st.text_area("Enter your practice prompt or topic:", height=100)
    
    if prompt:
        st.markdown(f"**Your prompt:** {prompt}")
        
        # Instructions
        st.markdown("**Instructions:**")
        st.markdown("- Speak out loud and practice your response")
        st.markdown("- Record yourself if possible")
        st.markdown("- Focus on clarity, pace, and confidence")
        
        # Timer section
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**⏱️ Set Practice Timer:**")
            duration = st.time_input("set tha alarm", value=None)
            if st.button("Start Timer"):
                st.success(f"Timer set for {duration} minutes! Start speaking now.")
        
        with col2:
            st.markdown("**📝 Self-Evaluation:**")
            if st.button("Complete Practice Session"):
                st.balloons()
                st.success("Great job! How did you feel about your practice?")
        
        # Self-reflection
        st.markdown("---")
        st.subheader("📋 Post-Practice Reflection")
        
        confidence = st.slider("How confident did you feel? (1-10)", 1, 10, 5)
        clarity = st.slider("How clear was your speech? (1-10)", 1, 10, 5)
        notes = st.text_area("Notes for improvement:", placeholder="What went well? What could be better?")
        
        if st.button("Save Practice Session"):
            st.success("Practice session recorded! Keep up the great work!")

st.markdown("---")
st.subheader("💪 Speaking Tips:")
st.markdown("""
- **Breathe deeply** before you start
- **Speak slowly** and clearly
- **Make eye contact** (even with yourself in a mirror)
- **Use gestures** naturally
- **Practice regularly** for best results
""")
