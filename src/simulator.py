import keyboard

pressed = False


def press_key(key):
    global pressed

    if not pressed:
        keyboard.press(key)
        pressed = True


def release_key(key):
    global pressed

    if pressed:
        keyboard.release(key)
        pressed = False
