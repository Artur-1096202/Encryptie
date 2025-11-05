from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

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

def main():
    print("Welkom bij de tekstversleutelaar\n")
    choice = input("Wil je (1) versleutelen of (2) ontsleutelen? Voer 1 of 2 in: ")

    if choice == '1':
        text = input("Voer hier de tekst in die je wilt versleutelen: ")
        password = input("Voer hier een wachtwoord in: ")
        encrypted = encrypt_with_fernet(text, password)
        print("Versleutelde tekst:\n", encrypted)

    elif choice == '2':
        token = input("Voer hier de versleutelde tekst in: ")
        password = input("Voer hier het wachtwoord in: ")
        try:
            decrypted = decrypt_with_fernet(token, password)
            print("Ontsleutelde tekst:\n", decrypted)
        except Exception as decrypt_error:
            print("Het ontsleutelen is mislukt. Controleer je wachtwoord en probeer het opnieuw.")
    else:
        print("Ongeldige keuze!")



if __name__ == '__main__':
    main()