import tempfile
import os
import shutil
from typing import Optional

def save_uploaded_audio(uploaded_file, target_filename: Optional[str] = None) -> str:
    if target_filename is None:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        target_filename = temp_file.name
        temp_file.close()
    
    with open(target_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    print(f"Audio file saved to {target_filename}")
    return target_filename

def create_temp_audio_file() -> str:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp_filename = temp_file.name
    temp_file.close()
    return temp_filename

def cleanup_audio_file(file_path: str):
    try:
        if file_path and os.path.exists(file_path):
            os.unlink(file_path)
            print(f"Cleaned up audio file: {file_path}")
    except Exception as e:
        print(f"Error cleaning up audio file: {e}")

def record_temp(duration=5, fs=44100):
    """Legacy function for compatibility - now just creates temp file path"""
    return create_temp_audio_file()
