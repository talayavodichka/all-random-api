import hashlib
import base64
import uuid
from datetime import datetime, timedelta

def generate_bool(seed: str) -> bool:
    return hashlib.sha256(seed.encode()).digest()[0] % 2 == 0

def generate_digit(seed: str) -> int:
    return hashlib.sha256(seed.encode()).digest()[0] % 10

def generate_char(seed: str) -> int:
    return hashlib.sha256(seed.encode()).digest()[0] % 94 + 33

def generate_integer(seed: str, min_val: int = -2147483647, max_val: int = 2147483647) -> int:
    if min_val == max_val:
        return min_val
    return int(int.from_bytes(hashlib.sha256(seed.encode()).digest()[:16], byteorder="big") % (max_val - min_val + 1) + min_val)

def generate_float(seed: str, min_val: float = -2147483647.0, max_val: float = 2147483647.0) -> float:
    if min_val == max_val:
        return min_val
    max_53 = (1 << 53) - 1
    rand53 = int.from_bytes(hashlib.sha256(seed.encode()).digest()[:16], byteorder='big') & max_53
    return min_val + (rand53 / max_53) * (max_val - min_val)

def generate_hash(seed: str, algorithm: str = "sha256") -> str:
    return hashlib.new(algorithm, seed.encode()).hexdigest()

def generate_bytes(seed: str, length: int = 16) -> str:
    return base64.b64encode(hashlib.sha256(seed.encode()).digest()[:length]).decode()

def generate_timestamp(seed: str, days: int = 365) -> str:
    return str(datetime.now() - timedelta(days=int.from_bytes(hashlib.sha256(seed.encode()).digest()[:2], "big") % days))

def generate_color(seed: str) -> str:
    hashed = hashlib.sha256(seed.encode())
    return f"#{hashed.digest()[0]:02x}{hashed.digest()[1]:02x}{hashed.digest()[2]:02x}"

def generate_uuid(seed: str) -> str:
    return str(uuid.UUID(bytes=hashlib.sha256(seed.encode()).digest()[:16]))

def generate_password(seed: str, length: int = 12) -> str:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    return "".join(chars[b % len(chars)] for b in hashlib.sha256(seed.encode()).digest()[:length])

def random_choice(seed: str, items: str = "") -> str:
    arr = items.split(",")
    return arr[hashlib.sha256(seed.encode()).digest()[0] % len(arr)].strip()

def generate_ipv4(seed: str) -> str:
    hashed = hashlib.sha256(seed.encode()).digest()
    return f"{(hashed[0] % 254) + 1}.{hashed[1] % 256}.{hashed[2] % 256}.{hashed[3] % 256}"

def generate_coords(seed: str) -> tuple:
    hashed = hashlib.sha256(seed.encode()).digest()
    return (generate_float(str(hashed[0]), -90, 90), generate_float(str(~hashed[0]), -180, 180))
