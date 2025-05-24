"""
🎀🎀
Block microphone capture → WAV filepath.
Audio is recorded, and the function only returns the file path after capture is complete.
🎀🎀
"""
import sounddevice as sd
import soundfile as sf
from utils.logger import log
from utils.config import *

RATE = 16_000
CHANNELS = 1
FORMAT = "PCM_16"

def record_to_file(out_path: str, seconds: int = 5) -> str:
    log.info(f"Recording {seconds}s of audio to {out_path}")
    audio = sd.rec(int(seconds * RATE), samplerate=RATE, channels=CHANNELS)
    sd.wait()
    sf.write(out_path, audio, RATE, subtype=FORMAT)
    return out_path
