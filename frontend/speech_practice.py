import streamlit as st
import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from ai_service import AIService
from speech_service import SpeechService
from supabase_service import SupabaseService
from auth import check_authentication

check_authentication()

st.title("🗣️ Speech Practice")
st.markdown("Practice your speaking skills with AI-powered feedback by uploading your audio recordings.")

if 'ai_service' not in st.session_state:
    st.session_state.ai_service = AIService()

if 'speech_service' not in st.session_state:
    st.session_state.speech_service = SpeechService()

if 'supabase_service' not in st.session_state:
    st.session_state.supabase_service = SupabaseService()

if 'recording_file' not in st.session_state:
    st.session_state.recording_file = None

if 'transcription' not in st.session_state:
    st.session_state.transcription = None


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
        st.markdown("- Think about your response to the prompt")
        st.markdown("- Record yourself using your device's recording app")
        st.markdown("- Upload your audio file for AI analysis")
        st.markdown("- Focus on clarity, pace, and confidence")
        
        # Audio Upload section
        st.markdown("**🎤 Upload Your Audio Recording:**")
        
        uploaded_audio = st.file_uploader(
            "Choose an audio file", 
            type=['wav', 'mp3', 'm4a', 'ogg', 'flac'],
            help="Record yourself speaking and upload the audio file here. Supported formats: WAV, MP3, M4A, OGG, FLAC"
        )
        
        if uploaded_audio is not None:
            st.success(f"Audio file uploaded: {uploaded_audio.name}")
            
            if st.button("🔍 Analyze My Speech"):
                with st.spinner("Processing your audio and generating feedback..."):
                    try:
                        audio_file_path, transcribed_text = st.session_state.speech_service.process_uploaded_audio(uploaded_audio)
                        
                        if transcribed_text:
                            st.session_state.transcribed_text = transcribed_text
                            st.session_state.recording_file = audio_file_path
                            st.success("Audio processed successfully!")
                            st.rerun()
                        else:
                            st.error("Failed to transcribe audio. Please try a different file.")
                    except Exception as e:
                        st.error(f"Error processing audio: {e}")
        
        # Display transcription results
        st.markdown("**📝 Transcription Results:**")
        if hasattr(st.session_state, 'transcribed_text') and st.session_state.transcribed_text:
            st.text_area("Your transcribed speech:", 
                       value=st.session_state.transcribed_text, 
                       height=200, 
                       disabled=True)
            
            if st.button("🔄 Get AI Feedback"):
                with st.spinner("Getting AI feedback..."):
                    feedback_prompt = f"""
                    Analyze this speech for a {practice_type.lower()} practice session.
                    
                    Topic/Prompt: {prompt}
                    
                    Speech transcription: {st.session_state.transcribed_text}
                    
                    Please provide feedback on:
                    1. Content relevance and depth
                    2. Speaking clarity and pace
                    3. Areas for improvement
                    4. Strengths to build upon
                    """
                    
                    ai_feedback = st.session_state.ai_service.get_response(feedback_prompt, max_tokens=800)
                    if ai_feedback:
                        st.markdown("### 🤖 AI Feedback")
                        st.markdown(ai_feedback)
                        st.session_state.ai_feedback = ai_feedback
                    else:
                        st.error("Failed to get AI feedback. Please try again.")
        else:
            st.info("Upload and analyze an audio recording to see your transcription here.")
        
        # Self-reflection and saving
        st.markdown("---")
        st.subheader("📋 Post-Practice Reflection")
        
        confidence = st.slider("How confident did you feel? (1-10)", 1, 10, 5)
        clarity = st.slider("How clear was your speech? (1-10)", 1, 10, 5)
        notes = st.text_area("Notes for improvement:", placeholder="What went well? What could be better?")
        
        if st.button("💾 Save Practice Session", type="primary"):
            if hasattr(st.session_state, 'transcribed_text') and st.session_state.transcribed_text:
                try:
                    user_id = st.session_state.user.id
                    ai_feedback = getattr(st.session_state, 'ai_feedback', None)
                    
                    session_notes = f"Transcription: {st.session_state.transcribed_text}\n\n"
                    if ai_feedback:
                        session_notes += f"AI Feedback: {ai_feedback}\n\n"
                    session_notes += f"User Notes: {notes}"
                    
                    success = st.session_state.supabase_service.save_speech_session(
                        user_id=user_id,
                        practice_type=practice_type,
                        prompt=prompt,
                        confidence=confidence,
                        clarity=clarity,
                        notes=session_notes
                    )
                    
                    if success:
                        st.success("🎉 Practice session saved successfully!")
                        st.balloons()
                        
                        if hasattr(st.session_state, 'recording_file') and st.session_state.recording_file:
                            st.session_state.speech_service.cleanup_audio_file(st.session_state.recording_file)
                        
                        if hasattr(st.session_state, 'transcribed_text'):
                            delattr(st.session_state, 'transcribed_text')
                        if hasattr(st.session_state, 'ai_feedback'):
                            delattr(st.session_state, 'ai_feedback')
                        if hasattr(st.session_state, 'recording_file'):
                            delattr(st.session_state, 'recording_file')
                        
                        st.rerun()
                    else:
                        st.error("Failed to save session. Please try again.")
                except Exception as e:
                    st.error(f"Error saving session: {e}")
            else:
                st.warning("Please complete a speech analysis before saving.")

st.subheader("📚 Previous Practice Sessions")

try:
    user_id = st.session_state.user.id
    previous_sessions = st.session_state.supabase_service.get_speech_sessions(user_id, limit=5)
    
    if previous_sessions:
        for i, session in enumerate(previous_sessions):
            with st.expander(f"🎤 {session['practice_type']} - {session['created_at'][:10]}"):
                st.markdown(f"**Topic/Prompt:** {session['prompt']}")
                st.markdown(f"**Confidence Rating:** {session['confidence_rating']}/10")
                st.markdown(f"**Clarity Rating:** {session['clarity_rating']}/10")
                
                if session.get('notes'):
                    st.markdown("**Session Notes:**")
                    st.text_area(
                        "Notes", 
                        value=session['notes'], 
                        height=200, 
                        disabled=True, 
                        key=f"notes_{session['id']}"
                    )
                
                st.caption(f"Created: {session['created_at']}")
    else:
        st.info("No previous sessions found. Complete a practice session to see your history here!")
        
except Exception as e:
    st.error(f"Error loading previous sessions: {e}")
    st.info("Please complete a session to see your practice history.")
