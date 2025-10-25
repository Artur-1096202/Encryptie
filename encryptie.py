from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_key_from_password(password: str, salt: bytes) -> bytes:
    # Dit gebruikt PBKDF2HMAC om een sleutel uit het wachtwoord te genereren

    Password_to_key_generator = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
        backend=default_backend()
    )
    key = Password_to_key_generator.derive(password.encode())

    # Fernet vereist een base64-gecodeerde sleutel
    return base64.urlsafe_b64encode(key)


def encrypt_with_fernet(plaintext, password):
    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    token = fernet.encrypt(plaintext.encode())
    return base64.b64encode(salt + token).decode()

def main():



if __name__ == '__main__':
    main()