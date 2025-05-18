from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import numpy
import hashlib
import base64
import uuid
import os
import time

app = FastAPI()

@app.get("/det/random-bool")
def det_generate_bool(seed: str):
    return {"bool": hashlib.sha256(seed.encode()).digest()[0] % 2 == 0}

@app.get("/nondet/random-bool")
def nondet_generate_bool():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    return {"bool": hashlib.sha256(seed.encode()).digest()[0] % 2 == 0}

@app.get("/det/random-digit")
def det_generate_digit(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"digit": hashed[0] % 10}

@app.get("/nondet/random-digit")
def nondet_generate_digit():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"digit": hashed[0] % 10}

@app.get("/det/random-char")
def det_generate_char(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    char_code = hashed[0] % 94 + 33
    return {"char": chr(char_code)}

@app.get("/nondet/random-char")
def nondet_generate_char():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    char_code = hashed[0] % 94 + 33
    return {"char": chr(char_code)}

@app.get("/det/random-number")
def det_generate_number(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    number = int.from_bytes(hashed[:16], byteorder="big")
    return {"number": number}

@app.get("/nondet/random-number")
def nondet_generate_number():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    number = int.from_bytes(hashed[:16], byteorder="big")
    return {"number": number}

@app.get("/det/random-hash")
def det_generate_hash(seed: str, algorithm: str = "sha256"):
    try:
        h = hashlib.new(algorithm, seed.encode())
        return {"hash": h.hexdigest()}
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

@app.get("/nondet/random-hash")
def nondet_generate_hash(algorithm: str = "sha256"):
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    try:
        h = hashlib.new(algorithm, seed.encode())
        return {"hash": h.hexdigest()}
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

@app.get("/det/random-bytes")
def det_generate_bytes(seed: str, length: int = 16):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"bytes": base64.b64encode(hashed[:length]).decode()}

@app.get("/nondet/random-bytes")
def nondet_generate_bytes(length: int = 16):
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"bytes": base64.b64encode(hashed[:length]).decode()}

@app.get("/det/random-timestamp")
def det_generate_timestamp(seed: str, days: int = 365):
    hashed = hashlib.sha256(seed.encode()).digest()
    delta = timedelta(days=int.from_bytes(hashed[:2], "big") % days)
    return {"timestamp": str(datetime.now() - delta)}

@app.get("/nondet/random-timestamp")
def nondet_generate_timestamp(days: int = 365):
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    delta = timedelta(days=int.from_bytes(hashed[:2], "big") % days)
    return {"timestamp": str(datetime.now() - delta)}

@app.get("/det/random-color")
def det_generate_color(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"color": f"#{hashed[0]:02x}{hashed[1]:02x}{hashed[2]:02x}"}

@app.get("/nondet/random-color")
def nondet_generate_color():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"color": f"#{hashed[0]:02x}{hashed[1]:02x}{hashed[2]:02x}"}

@app.get("/det/random-uuid")
def det_generate_uuid(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"uuid": str(uuid.UUID(bytes=hashed[:16]))}

@app.get("/nondet/random-uuid")
def nondet_generate_uuid():
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"uuid": str(uuid.UUID(bytes=hashed[:16]))}

@app.get("/det/random-password")
def det_generate_password(seed: str, length: int = 12):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"password": "".join(chars[b % len(chars)] for b in hashed[:length])}

@app.get("/nondet/random-password")
def nondet_generate_password(length: int = 12):
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    hashed = hashlib.sha256(seed.encode()).digest()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    return {"password": "".join(chars[b % len(chars)] for b in hashed[:length])}

@app.get("/det/random-choice")
def det_random_choice(seed: str, items: str):
    arr = items.split(",")
    index = hashlib.sha256(seed.encode()).digest()[0] % len(arr)
    return {"choice": arr[index].strip()}

@app.get("/nondet/random-choice")
def nondet_random_choice(items: str):
    seed = str(datetime.now().timestamp()) + str(os.urandom(16))
    arr = items.split(",")
    index = hashlib.sha256(seed.encode()).digest()[0] % len(arr)
    return {"choice": arr[index].strip()}
