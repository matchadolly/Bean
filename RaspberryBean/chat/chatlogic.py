"""
🎀🎀
OpenAI's ChatGPT.
🎀🎀
"""
from openai import OpenAI
from utils.logger import log
from utils.config import *
import os
from pathlib import Path
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MEM_FILE = Path(__file__).with_name("memory.txt")
SYSTEM_PROMPT = "You are Bean, a cuddly companion."

def _read_memory() -> str:
    return MEM_FILE.read_text(encoding="utf-8") if MEM_FILE.exists() else ""

def chat(user_text: str) -> dict:
    log.info("Sending prompt to OpenAI")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\nMEMORY:\n" + _read_memory()},
        {"role": "user", "content": user_text},
        {"role": "assistant", "content": (
            "You MUST respond in valid JSON: "
            '{"reply": "...", "mood": "...", '
            '"should_write_memory": false, "memory_to_write": ""}'
        )}
    ]
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.8,
    )
    json_text = resp.choices[0].message.content.strip()
    return json.loads(json_text)
