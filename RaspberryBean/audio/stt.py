"""
🎀🎀
OpenAI's Whisper.
Sends a WAV file and returns the transcript.
🎀🎀
"""
from openai import OpenAI
from utils.logger import log
from utils.config import *  # ☁️ Loads .env on import.
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe(wav_path: str) -> str:
    log.info("Transcribing %s with Whisper…", wav_path)
    with open(wav_path, "rb") as f:
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="text",
            language="en"
        )
    return resp
