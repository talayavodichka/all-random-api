from fastapi import APIRouter, Query, HTTPException
from utils import generators

router = APIRouter(prefix="/det")

@router.get("/random-bool")
async def det_bool(seed: str = Query(...)):
    return {"bool": generators.generate_bool(seed)}

@router.get("/random-digit")
async def det_digit(seed: str = Query(...)):
    return {"digit": generators.generate_digit(seed)}

@router.get("/random-char")
async def det_char(seed: str = Query(...)):
    return {"char": generators.generate_char(seed)}

@router.get("/random-integer")
async def det_integer(seed: str = Query(...), min_val: int = -2147483647, max_val: int = 2147483647):
    return {"integer": generators.generate_integer(seed, min_val, max_val)}

@router.get("/random-float")
async def det_float(seed: str = Query(...), min_val: float = -2147483647.0, max_val: float = 2147483647.0):
    return {"float": generators.generate_float(seed, min_val, max_val)}

@router.get("/random-string")
async def det_string(seed: str = Query(...), length: int = 12):
    return {"string": generators.generate_string(seed, length)}

@router.get("/random-hash")
async def det_hash(seed: str = Query(...), algorithm: str = "sha256"):
    try:
        return {"hash": generators.generate_hash(seed, algorithm)}
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

@router.get("/random-bytes")
async def det_bytes(seed: str = Query(...), length: int = 16):
    return {"bytes": generators.generate_bytes(seed, length)}

@router.get("/random-timestamp")
async def det_timestamp(seed: str = Query(...), days: int = 365):
    return {"timestamp": generators.generate_timestamp(seed, days)}

@router.get("/random-color")
async def det_color(seed: str = Query(...)):
    return {"color": generators.generate_color(seed)}

@router.get("/random-uuid")
async def det_uuid(seed: str = Query(...)):
    return {"uuid": generators.generate_uuid(seed)}

@router.get("/random-password")
async def det_password(seed: str = Query(...), length: int = 12):
    return {"password": generators.generate_password(seed, length)}

@router.get("/random-choice")
async def det_choice(seed: str = Query(...), items: str = ""):
    return {"choice": generators.random_choice(seed, items)}

@router.get("/random-ipv4")
async def det_ipv4(seed: str = Query(...)):
    return {"ipv4": generators.generate_ipv4(seed)}

@router.get("/random-ipv6")
async def det_ipv6(seed: str = Query(...)):
    return {"ipv6": generators.generate_ipv6(seed)}

@router.get("/random-coords")
async def det_coords(seed: str = Query(...)):
    return {"coords": generators.generate_coords(seed)}
