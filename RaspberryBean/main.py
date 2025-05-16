"""
🎀
BEAN'S HEART AND SOUL.
Run: python ~/Bean/RaspberryBean/main.py
🎀
"""
#!/usr/bin/env python3
from utils.logger import log
from audio.record import record_to_file
from audio.tts import speak
from chat.chatlogic import chat
from vision.display import show_gif
from hardware.button import on_press
from audio.stt import transcribe
import tempfile

STATE = "IDLE"

def handle_press():
    global STATE
    if STATE != "IDLE":
        return
    STATE = "RECORDING"
    show_gif("vision/faces/neutral_talk.gif")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    record_to_file(tmp.name, seconds=5)
    text = transcribe(tmp.name)
    reply = chat(text)["reply"]  
    STATE = "THINKING"
    reply = chat(open(tmp.name, "rb").name)["reply"]
    STATE = "SPEAKING"
    speak(reply)
    STATE = "IDLE"
    show_gif("vision/faces/neutral_rest.gif")

def main():
    log.info("Bean starting in IDLE")
    on_press(handle_press)
    # 🎀 Run for ever!
    import signal, time
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
