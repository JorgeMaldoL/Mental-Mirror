import sounddevice as sd
from scipy.io.wavfile import write

def record(filename="recording.wav", duration=5, fs=44100):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
