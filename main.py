from fastapi import FastAPI, HTTPException
import hashlib
import base64

app = FastAPI()

@app.get("/random-number")
def generate_number(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    number = int.from_bytes(hashed[:16], byteorder="big")
    return {"random_number": number}

@app.get("/random-bytes")
def generate_bytes(seed: str, length: int = 16):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"random_bytes": base64.b64encode(hashed[:length]).decode()}

@app.get("/random-char")
def generate_char(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    char_code = hashed[0] % 94 + 33
    return {"random_char": chr(char_code)}

@app.get("/random-digit")
def generate_digit(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    return {"random_digit": hashed[0] % 10}