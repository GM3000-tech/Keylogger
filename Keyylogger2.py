from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    print("\n=== Decrypted Log Output ===\n")
    print(decrypted_data.decode())

if __name__ == "__main__":
    path = input("Enter path to encrypted log file (e.g. logs/log_2025-08-04_15-32-12.txt): ")
    decrypt_file(path)
