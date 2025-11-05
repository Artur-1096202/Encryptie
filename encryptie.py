from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import pyperclip
import threading
import time

def generate_key_from_password(password: str, salt: bytes) -> bytes:
    if not password:
        raise ValueError("Wachtwoord mag niet leeg zijn.")


    # Dit gebruikt PBKDF2HMAC om een sleutel uit het wachtwoord te genereren

    Password_to_key_generator = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=300000,
        backend=default_backend()
    )
    key = Password_to_key_generator.derive(password.encode())

    # Fernet vereist een base64-gecodeerde sleutel
    return base64.urlsafe_b64encode(key)


def encrypt_with_fernet(plaintext, password):
    if not plaintext:
        raise ValueError("Tekst mag niet leeg zijn.")

    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    token = fernet.encrypt(plaintext.encode())
    return base64.b64encode(salt + token).decode()


def decrypt_with_fernet(token_b64, password):
    data = base64.b64decode(token_b64)
    salt = data[:16]
    token = data[16:]
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(token)
    return decrypted.decode()


def copy_to_clipboard_with_timeout(text, timeout=30):
    """Dit kopieert een tekst naar de klembord en leegt het na een aantal seconden"""

    pyperclip.copy(text)
    print(f"\nDe tekst is gekopieerd naar het klembord. Het wordt over {timeout} seconden geleegd.")

    def clear_clipboard():
        time.sleep(timeout)
        pyperclip.copy("")
        print("Het klembord is nu automatisch geleegd.")

    threading.Thread(target=clear_clipboard, daemon=True).start()

def main():
    print("=== Welkom bij de Symmetrische Encryptie Tool (AES-256 / Fernet) ===")
    choice = input("1 = Encryptie | 2 = Decryptie\nKeuze: ")

    if choice == '1':
        text = input("Voer hier de tekst in die je wilt versleutelen: ")
        password = input("Voer hier een wachtwoord in: ")
        try:
            encrypted = encrypt_with_fernet(text, password)
            print("\nVersleutelde tekst:\n", encrypted)

            # Dit kopieert naar de klembord met automatische leegmaak na 30 seconden
            copy_to_clipboard_with_timeout(encrypted, timeout=30)

        except Exception as error:
            print("Fout: Er ging iets mis. Controleer je invoer en probeer opnieuw.")
            print("Details:", error)


    elif choice == '2':
        token = input("Voer hier de versleutelde tekst in: ")
        password = input("Voer hier het wachtwoord in: ")
        try:
            decrypted = decrypt_with_fernet(token, password)
            print("\nOntsleutelde tekst:\n", decrypted)

            # Dit kopieert naar de klembord met automatische leegmaak na 30 seconden
            copy_to_clipboard_with_timeout(decrypted, timeout=30)

        except Exception:
            print("Het ontsleutelen is mislukt. Controleer je wachtwoord en probeer het opnieuw.")
    else:
        print("Ongeldige keuze!")



if __name__ == '__main__':
    main()