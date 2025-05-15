# Bean
Here lies the documentation of my actions, both intentional and accidental, made solely to prevent future me from staring blankly into the chaos of my own incompetence... This is a work in progress... everything is probably broken.

## 1. Requirements
### 1.1 Physical components
Component | Purpose
--- | ---
[Raspberry Pi 5 (4 GB)](https://www.amazon.co.uk/dp/B0CK3L9WD3) | Computing
[Raspberry Pi active cooler](https://www.amazon.co.uk/dp/B0CLXZBR5P) | Cooling
[SanDisk 32 GB memory card](https://www.amazon.co.uk/dp/B06XYHN68L) | Storage
[Pimoroni HyperPixel 4.0 Square Touch](https://www.amazon.co.uk/dp/B07V9K54WV) | Display
[Mini USB microphone](https://www.amazon.co.uk/dp/B0DCZ9M6RV) | Audio in
[Adafruit STEMMA speaker & audio amplifier](https://www.amazon.co.uk/dp/B082MNXJG5) | Audio out
[Waveshare USB sound card (external audio converter)](https://www.amazon.co.uk/dp/B08R38TXXL) | Audio out
(Not purchased yet) Momentary push-button |
(Not purchased yet) Power bank (Anker Nano Power Bank A1653 5000 mAh, 5V 3A PD out) |
[Adafruit female-female jumper wires (75mm)](https://www.amazon.co.uk/dp/B071YNFGBR) |
[USB AMale-AFemale extension cables](https://www.amazon.co.uk/dp/B09LYRRQ91) |
[JST PH2.0 connector cables](https://www.amazon.co.uk/dp/B091FHPN1X) |

I used a Mac for the Imager etc.

### 1.2 Software and services
Service | Purpose
--- | ---
OpenAI API | Whisper for speech recognition, ChatGPT for conversation.
Google Chirp API | I might use this for speech recognition instead of Whisper, after determining which has lower latency.
ElevenLabs API | Speech generation.
Raspberry Pi Imager | Flashes the SD card.

## 2. The actual nitty gritty
### 2.1 Initial setup
1. Plug an SD card into your computer. Flash the Raspberry Pi OS with Pi Imager.
   1. Raspberry Pi Device: Raspberry Pi 5.
   2. Operating System: Raspberry Pi OS Lite (64-bit).
   3. Storage: Choose your SD card.
   4. OS Customisation:
      1. Set hostname: bean.local
      2. Set username and password: bean (username), bean (password).
      3. Configure wireless LAN: enter your wifi's SSID and password.
      4. Enable SSH, Use password authentication.
      5. Play sound when finished.
2. Insert the SD card into your Pi. Connect the active cooler, then the HyperPixel screen. Connect the Pi to power. A green LED should light for ~20s when the kernel loads. The fan will be VERY loud and you may smell SMOKE and occasionally the LED will turn red but APPARENTLY this is normal. I think. Everything since has been fine. Then the LED idles and stays green and the wifi firmware is loaded.
3. Set further initial configs. [Code](https://github.com/matchadolly/Bean/blob/24a24d0f58b4ea604729f6c7e5683276512e8c35/Initial%20setup%20configs).
4. You may try to connect to eduroam if you want. I FAILED 😭. I shall attempt to do this again later. [HORRIBLE BROEKN Code](https://github.com/matchadolly/Bean/blob/9903d74072f5c1adbb7c5babb92627f7f4545103/Connect%20to%20eduroam).
5. Test to see whether the peripherals work. [Code](https://github.com/matchadolly/Bean/blob/e74847fb253be7dbcd22d8fc8ba5485866d700f9/Peripheral%20tests).
### 2.2 Planned project file structure
	Bean/
 		main.py
	 	settings.json  # 🎀 Can be edited by user.
	 	memory.txt  # 🎀 One fact per line.
	 	faces/  # 🎀 PNG frames for each mood. Could use MP4 or GIF instead?
	 		happy_0.png
			happy_1.png
	 	systemd/bean.service
Create the directories `mkdir -p ~/bean/{faces,systemd}`
### 2.3 Core loop (python skeleton)
NOT the full code, just the very basic logic. [Code](https://github.com/matchadolly/Bean/blob/dfc2127b9ef422b7bd7f65b778a547f716c1c584/main.py)
