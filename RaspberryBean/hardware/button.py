"""
🎀🎀
Touch-button handler for the HyperPixel.
It watches the device in a background thread.
When you lift your finger inside the BUTTON_RECT, all registered callbacks fire.
🎀🎀
"""
from utils.logger import log
from threading import Thread
from evdev import InputDevice, categorize, ecodes, list_devices

# 🎀🎀 ---------- Config ---------- 🎀🎀

# 🎀 This is the rectangle of the speak button (x1, y1, x2, y2).
BUTTON_RECT = (20, 580, 140, 700)

# 🎀 If you're unsure which /dev/input/eventN is the HyperPixel, run "python -m evdev.evtest" and tap the screen.
def _find_touch_device() -> str:
    for path in list_devices():
        dev = InputDevice(path)
        if "HyperPixel" in dev.name or "Touchscreen" in dev.name:
            return path
    raise RuntimeError("Touch event device not found :( Run evtest to locate it.")

TOUCH_DEV_PATH = _find_touch_device()

# 🎀🎀 ---------- Actual code ---------- 🎀🎀

_callbacks = []

def on_press(fn):
    """ ☁️ Registers a zero argument func to call when the speak button is pressed. ☁️ """
    _callbacks.append(fn)

def _event_loop():
    dev = InputDevice(TOUCH_DEV_PATH)
    log.info("Listening to touch events on %s (%s)", TOUCH_DEV_PATH, dev.name)
    x = y = None
    touching = False
    for event in dev.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_MT_POSITION_X:
                x = event.value
            elif event.code == ecodes.ABS_MT_POSITION_Y:
                y = event.value
        elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH:
            if event.value == 1:  # ☁️ Finger down.
                touching = True
            else:  # ☁️ Finger lifted.
                if touching and x is not None and y is not None:
                    inside = (BUTTON_RECT[0] <= x <= BUTTON_RECT[2] and
                              BUTTON_RECT[1] <= y <= BUTTON_RECT[3])
                    if inside:
                        log.info("Speak button tapped at (%d, %d)", x, y)
                        for fn in _callbacks:
                            try:
                                fn()
                            except Exception as e:
                                log.error("Callback error: %s", e)
                touching = False

# 🎀 Starts background listener as soon as this module imports.
Thread(target=_event_loop, daemon=True).start()
