from cryptography.fernet import Fernet
import os

def encrypt_data(data):
    # Safe: uses strong encryption and loads key from env
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        raise ValueError("Missing ENCRYPTION_KEY")
        
    f = Fernet(key.encode())
    return f.encrypt(data.encode())
