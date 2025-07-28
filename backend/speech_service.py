from ai_service import AIService
from record_logic import save_uploaded_audio, create_temp_audio_file, cleanup_audio_file
import os
from typing import Optional

class SpeechService:
    def __init__(self):
        self.ai_service = AIService()
    
    def process_uploaded_audio(self, uploaded_file) -> tuple[Optional[str], Optional[str]]:
        """
        Process an uploaded audio file and return the file path and transcription.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            tuple: (audio_file_path, transcribed_text)
        """
        try:
            audio_file = save_uploaded_audio(uploaded_file)
            transcribed_text = self.ai_service.transcribe_audio(audio_file)
            return audio_file, transcribed_text
        except Exception as e:
            print(f"Error processing uploaded audio: {e}")
            return None, None
    
    def cleanup_audio_file(self, audio_file_path: str):
        """Clean up temporary audio file"""
        cleanup_audio_file(audio_file_path)
    
    def analyze_speech(self, audio_file_path: str, analysis_prompt: str) -> Optional[str]:
        """
        Analyze speech from an audio file using AI.
        
        Args:
            audio_file_path: Path to the audio file
            analysis_prompt: Prompt for AI analysis
            
        Returns:
            str: AI analysis of the speech
        """
        try:
            transcribed_text = self.ai_service.transcribe_audio(audio_file_path)
            if not transcribed_text:
                return None
            full_prompt = f"{analysis_prompt}\n\nTranscribed Speech: {transcribed_text}"
            return self.ai_service.get_response(full_prompt)
        except Exception as e:
            print(f"Error in analyze_speech: {e}")
            return None
