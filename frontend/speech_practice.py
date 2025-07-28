import streamlit as st
import datetime
import sys
import os

# Add backend to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from timer_logic import TimerLogic

st.title("🗣️ Speech Practice")
st.markdown("Practice your speaking skills, whether it's for presentations, interviews, or general communication improvement.")

# Initialize timer in session state
if 'timer_logic' not in st.session_state:
    st.session_state.timer_logic = TimerLogic()


practice_type = st.selectbox(
    "What would you like to practice?",
    ["Public Speaking", "Interview Preparation", "Presentation Skills", "Conversation Practice", "Debate/Argumentation"]
)

if practice_type:
    st.markdown(f"**Practicing: {practice_type}**")
    
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
        
        st.markdown("**Instructions:**")
        st.markdown("- Speak out loud and practice your response")
        st.markdown("- Record yourself")
        st.markdown("- Focus on clarity, pace, and confidence")
        
        # Timer section
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**⏱️ Set Practice Timer:**")
            
            # Use number inputs for minutes and seconds
            col_min, col_sec = st.columns([1, 1])
            with col_min:
                timer_minutes = st.number_input("Minutes", min_value=0, max_value=60, value=3, step=1)
            with col_sec:
                timer_seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1)
            
            # Calculate total time in minutes (with decimal for seconds)
            total_minutes = timer_minutes + (timer_seconds / 60.0)
            
            # Timer control buttons
            col_start, col_stop = st.columns([1, 1])
            
            with col_start:
                if st.button("Start Timer"):
                    if total_minutes > 0:
                        st.session_state.timer_logic.start(total_minutes)
                        if timer_seconds > 0:
                            st.success(f"Timer started for {timer_minutes}m {timer_seconds}s! Start speaking now.")
                        else:
                            st.success(f"Timer started for {timer_minutes} minutes! Start speaking now.")
                        st.rerun()
                    else:
                        st.warning("Please set a timer duration greater than 0.")
            
            with col_stop:
                if st.session_state.timer_logic.is_running:
                    if st.button("Stop Timer"):
                        st.session_state.timer_logic.stop()
                        st.info("Timer stopped.")
                        st.rerun()
                else:
                    st.button("Stop Timer", disabled=True)
            
            # Display countdown if timer is running
            if st.session_state.timer_logic.is_running:
                timer_status = st.session_state.timer_logic.get_remaining_time()
                mins = timer_status['minutes']
                secs = timer_status['seconds']
                
                if mins > 0 or secs > 0:
                    st.markdown(f"**⏰ Time Remaining: {mins:02d}:{secs:02d}**")
                    # Auto-refresh every second
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("⏰ Time's up! Practice session complete!")
                    st.balloons()
                    # Reset timer
                    st.session_state.timer_logic.stop_timer()
        
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
