import os

def get_shared_secret():
    return os.getenv("SHARED_SECRET", "b01lersctf2025")