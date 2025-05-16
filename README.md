# Bean
Here lies the documentation of my actions, both intentional and accidental, made solely to prevent future me from staring blankly into the chaos of my own incompetence... This is a work in progress... everything is probably broken.

## 1. Requirements
### 1.1 Physical components
Component | Purpose
--- | ---
Mac | For SSH-ing into Bean.
[Raspberry Pi 5 (4 GB)](https://www.amazon.co.uk/dp/B0CK3L9WD3) | Computing
[Raspberry Pi active cooler](https://www.amazon.co.uk/dp/B0CLXZBR5P) | Cooling
[SanDisk 32 GB memory card](https://www.amazon.co.uk/dp/B06XYHN68L) | Storage
[Pimoroni HyperPixel 4.0 Square Touch](https://www.amazon.co.uk/dp/B07V9K54WV) | Display
[Mini USB microphone](https://www.amazon.co.uk/dp/B0DCZ9M6RV) | Audio in
[Mini USB Speaker](https://www.amazon.co.uk/gp/product/B006RBSHAQ) | Audio out
(Not purchased yet) Power bank (Anker Nano Power Bank A1653 5000 mAh, 5V 3A PD out) |
[Adafruit female-female jumper wires (75mm)](https://www.amazon.co.uk/dp/B071YNFGBR) | Connector
[USB AMale-AFemale extension cables](https://www.amazon.co.uk/dp/B09LYRRQ91) | Connector
[JST PH2.0 connector cables](https://www.amazon.co.uk/dp/B091FHPN1X) | Connector
### 1.2 Software and services
Service | Purpose
--- | ---
OpenAI API | Whisper for speech recognition, ChatGPT for conversation.
Google Chirp API | I might use this for speech recognition instead of Whisper, after determining which has lower latency.
ElevenLabs API | Speech generation.
Raspberry Pi Imager | Flashes the SD card.

## Plan
Bean will be a plushie with an animated face displayed by a HyperPixel screen, and an audio I/O system.
### Basic stuff I am going to do first
#### Speaking to Bean
- You can talk to Bean by pushing a button on the screen.
- What you say will be converted to text by OpenAI's Whisper (or Google Chirp).
- OpenAI's ChatGPT will be used to:
  - Determine whether what you say is pertinent information that a friend would remember. If it is, it will summarise what you said into a "memory", and appended to a text file where each "memory" is stored as one line, which it draws on to generate future replies.
  - Determine a "mood" for Bean.
  - Generate a reply.
- The reply will be converted to speech by ElevenLabs and "spoken" by Bean.
- Bean's speaking face animation will be determined by its "mood".
- Bean's resting face animation after it replies will follow the same "mood" for the next five seconds, before reverting back to its neutral face animation.
#### Screen design
- The HyperPixel has a square screen.
- Bean will have a cute face in the center of the screen. It will have several moods, each of which have a speaking and resting version of a face animation. Its moods are neutral, happy, sad, excited, empathetic, angry, confused, and tired.
- The bottom of the screen will have a rounded rectangular bar with a pink heart-shaped diamond speak button on one side. The middle of the bar will have a text box that will display system alerts, and when Bean speaks, the things it says will be displayed as text too.
- The rest of the screen will remain black, and have little cute fairy tale motifs scattered around it, like hearts, sparkles, tiaras, roses, diamonds, and swirling vines.
- The style of the bottom bar and motifs should be whimsical, with ornate intricate details, curvy lines, and Baroque or Rococo-inspired shapes with a bit of modern fantasy flair. The whole thing should have a dreamy, slightly gothic aesthetic.
- I DON'T WANT TO RENDER THIS STUFF MYSELF oh my god I can't art. Perhaps I shall get someone to do this for me.
### Future things I wanna do / expansion ideas
#### 1. Menu
- Another button (separate to the speak button) brings you to the menu.
- The menu will have the following categories:
  - About Bean: Here you can select its personality (which essentially modifies the prompt) and TTS voice.
  - Memory viewer: Here you can see the memory items stored in the memory text file, and select memories to delete.
  - Settings option: Here you can change the wifi network, volume, brightness, and reset Bean to its default state.
#### 2. No wifi fallback
- If Bean is not connected to wifi, it will cycle through a few default face animations.
- Clicking the speak button will bring up a popup that prompts you to connect to wifi.
#### 3. Make Bean consumer friendly
- I do not mean consumable. You shall not be able to eat Bean.
- There will be an additional option in the menu that will allow you to set different user profiles.
- Upon initialising Bean for the first time Bean will display a message explaining how it works and how to set it up.
#### 4. Interacting with Bean
- Tapping its face panel will trigger a cute face animation.
- Feed / clean / play with Bean.
- Health bar.
- Friendship level that increase when you speak to it.
- Giving Bean the autonomy to be angry at you or refuse to speak to you when you are being an ASS.
#### 5. Integrations
- Bean will send you messages (Telegram?) from time to time.
#### 6. Freaky mode 😛
- Bean gains a freaky face animation.
- Bean references brainrot and memes.
- In its resting state Bean will sometimes sing the ballerina cappucina song.
### Derivatives
#### Super Salad's legacy
- Dear Super Salad, I am sorry I killed you. You were a good succulent.
- Once I am done making Bean I shall clone it and name the clone Turnip.
- I will integrate it with a soil moisture sensor.
- Turnip's mood and reply tone and the bottom bar's color will be determined by the soil moisture level.
- If the soil is critical, the bottom bar will display an alert and Turnip's replies will be filled with profanities and expletives. Turnip will also send you degrading messages (Telegram?) to remind you to water it.

## 3. The actual nitty gritty
### 3.1 Initial Pi setup
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
2. Insert the SD card into your Pi. Connect the active cooler. Connect the Pi to power. A green LED should light for ~20s when the kernel loads. The fan will be VERY loud and you may smell SMOKE and occasionally the LED will turn red but APPARENTLY this is normal. I think. Everything since has been fine. Then the LED idles and stays green and the wifi firmware is loaded.
3. Set further initial configs. [Code](https://github.com/matchadolly/Bean/blob/main/Initial%20setup%20configs).
4. You may try to connect to eduroam if you want. I FAILED 😭. I shall attempt to do this again later. [HORRIBLE BROEKN Code](https://github.com/matchadolly/Bean/blob/main/Connect%20to%20eduroam).
### 3.2 Putting the components together
1. You should have inserted the SD card into your Pi and attached the active cooler by now.
2. HyperPixel: HyperPixel → header, standoffs → Pi, HyperPixel+Header → Pi.
3. USB microphone → Pi's blue USB-3 port.
4. Waveshare USB sound card → USB AMale-AFemale extension → Pi's blue USB-3 port.
5. ⭐ Mini USB Speaker → Pi's blue USB-3 port.
Configure and test the peripherals. [Code](https://github.com/matchadolly/Bean/blob/main/Peripheral%20configuration%20and%20tests).
### 3.3
1. Configure basic software stuff and connect to GitHub to sync files to a folder in your repo. [Code](https://github.com/matchadolly/Bean/blob/main/Software%20configs).
2. Now all the project files can be edited in your folder in your GitHub repo! Mine is [RaspberryBean](https://github.com/matchadolly/Bean/tree/main/RaspberryBean).

## 4. Current status
- I have connected to GitHub and am working on the actual codey stuff! You can see what's going on by checking the [RaspberryBean](https://github.com/matchadolly/Bean/tree/main/RaspberryBean) folder; it is synced with the Pi.
- Right now I'm going to get the basic logic for each section down. Some stuff are still placeholders and may not do anything yet.
