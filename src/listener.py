import keyboard
import time

from src.settings import INPUT_KEY, OUTPUT_KEY, CHECK_DELAY
from src.simulator import press_key, release_key


def start():

    while True:

        if keyboard.is_pressed(INPUT_KEY):
            press_key(OUTPUT_KEY)

        else:
            release_key(OUTPUT_KEY)

        time.sleep(CHECK_DELAY)
