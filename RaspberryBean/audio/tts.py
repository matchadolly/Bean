"""
🎀🎀
ElevenLabs' TTS.
🎀🎀
"""
from elevenlabs import generate, play, set_api_key
from utils.logger import log
from utils.config import *
import os

VOICE_ID = "REPLACE"
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def speak(text: str) -> None:
    log.info("Generating speech (%s chars)", len(text))
    audio = generate(text=text, voice=VOICE_ID, stream=True)
    play(audio)
    