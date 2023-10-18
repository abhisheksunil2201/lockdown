from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        with open("encryption_key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Encryption key not found. Generate a key using 'generate_key()'.")


def initialize_fernet():
    key = load_key()
    if key:
        return Fernet(key)


def encrypt_file(fernet, input_filename, output_filename):
    try:
        with open(input_filename, "rb") as file:
            plaintext = file.read()
        encrypted_data = fernet.encrypt(plaintext)
        with open(output_filename, "wb") as file:
            file.write(encrypted_data)
        print(
            f"File '{input_filename}' encrypted and saved as '{output_filename}'.")
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")

# Decrypt a file


def decrypt_file(fernet, input_filename, output_filename):
    try:
        with open(input_filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(output_filename, "wb") as file:
            file.write(decrypted_data)
        print(
            f"File '{input_filename}' decrypted and saved as '{output_filename}'.")
    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
