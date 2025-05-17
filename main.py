from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import hashlib
import base64
import uuid

app = FastAPI()

@app.get("/random-bool")
def generate_bool(seed: str):
    return {"bool": hashlib.sha256(seed.encode()).digest()[0] % 2 == 0}

@app.get("/random-digit")
def generate_digit(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"digit": hashed[0] % 10}

@app.get("/random-char")
def generate_char(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    char_code = hashed[0] % 94 + 33
    return {"char": chr(char_code)}

@app.get("/random-number")
def generate_number(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    number = int.from_bytes(hashed[:16], byteorder="big")
    return {"number": number}

@app.get("/random-hash")
def generate_hash(seed: str, algorithm: str = "sha256"):
    try:
        h = hashlib.new(algorithm, seed.encode())
        return {"hash": h.hexdigest()}
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

@app.get("/random-bytes")
def generate_bytes(seed: str, length: int = 16):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"bytes": base64.b64encode(hashed[:length]).decode()}

@app.get("/random-timestamp")
def generate_timestamp(seed: str, days: int = 365):
    hashed = hashlib.sha256(seed.encode()).digest()
    delta = timedelta(days=int.from_bytes(hashed[:2], "big") % days)
    return {"timestamp": str(datetime.now() - delta)}

@app.get("/random-color")
def generate_color(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"color": f"#{hashed[0]:02x}{hashed[1]:02x}{hashed[2]:02x}"}

@app.get("/random-uuid")
def generate_uuid(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"uuid": str(uuid.UUID(bytes=hashed[:16]))}

@app.get("/random-password")
def generate_password(seed: str, length: int = 12):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"password": "".join(chars[b % len(chars)] for b in hashed[:length])}

@app.get("/random-choice")
def random_choice(seed: str, items: str):
    arr = items.split(",")
    index = hashlib.sha256(seed.encode()).digest()[0] % len(arr)
    return {"choice": arr[index].strip()}