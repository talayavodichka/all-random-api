from fastapi import FastAPI, HTTPException
import hashlib

app = FastAPI()

@app.get("/random-number")
def generate_number(seed: str):
    hashed = hashlib.sha256(seed.encode()).digest()
    number = int.from_bytes(hashed[:16], byteorder="big")
    
    return {
        "seed": seed,
        "random_number": number,
        "bit_length": number.bit_length()
    }