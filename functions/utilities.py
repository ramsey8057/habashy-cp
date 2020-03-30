import hashlib

def encrypt(passwd):
    return hashlib.md5(passwd.encode()).hexdigest()
