import ui
from encryption import generate_key, initialize_fernet, encrypt_file, decrypt_file


def main():
    password_ui = ui.show_password_prompt()
    result = password_ui.result
    print("Password correct:", result)
    if result:
        print("Decrypting files...")
        decrypt_file()


if __name__ == "__main__":
    main()
