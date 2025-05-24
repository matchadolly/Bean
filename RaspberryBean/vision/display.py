"""
🎀🎀
Currently only logs calls. Display code will be added later.
🎀🎀
"""
from utils.logger import log

def show_gif(path: str, loop_once: bool = False) -> None:
    log.info("Would display GIF: %s (loop_once=%s)", path, loop_once)
    