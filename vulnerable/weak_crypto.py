import hashlib

def hash_password(password):
    # Vulnerable: uses weak MD5 hash
    hasher = hashlib.md5()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()
