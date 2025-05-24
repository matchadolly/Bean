"""
🎀🎀
A centralised and colorised logger for Bean!
To use:
    from utils.logger import log
    log.info("Hello")
🎀🎀
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger("raspberrybean")
