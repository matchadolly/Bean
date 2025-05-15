import os, json, time, asyncio, sounddevice as sd, tempfile
from openai import OpenAI
from elevenlabs import generate, save
from gpiozero import Button
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

# 🎀 ---------- Config ----------
api = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ELEVEN_KEY = os.getenv("ELEVEN_API_KEY")
PTT = Button(17)
MENU = Button(27)
MEM_FILE = "memory.txt"
SETTINGS = json.load(open("settings.json"))
MOODS = ["neutral", "happy", "sad", "excited", "sleepy"]
# 🎀 ---------- Config ----------
