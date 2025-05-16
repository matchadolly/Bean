"""
🎀
Block microphone capture → WAV filepath.
🎀
"""
import sounddevice as sd
import soundfile as sf
from utils.logger import log
from utils.config import *  # noqa: F401 (side-effect)

RATE = 16_000  # 16 kHz
CHANNELS = 1
FORMAT = "PCM_16"

def record_to_file(out_path: str, seconds: int = 5) -> str:
    log.info(f"Recording {seconds}s of audio to {out_path}")
    audio = sd.rec(int(seconds * RATE), samplerate=RATE, channels=CHANNELS)
    sd.wait()
    sf.write(out_path, audio, RATE, subtype=FORMAT)
    return out_path
