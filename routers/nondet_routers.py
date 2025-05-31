from fastapi import APIRouter, HTTPException
from utils import generators, seed_manager

router = APIRouter(prefix="/nondet")

@router.get("/random-bool")
async def nondet_bool():
    seed = seed_manager.get_seed_by_time()
    return {"bool": generators.generate_bool(seed)}

@router.get("/random-digit")
async def nondet_digit():
    seed = seed_manager.get_seed_by_time()
    return {"digit": generators.generate_digit(seed)}

@router.get("/random-char")
async def nondet_char():
    seed = seed_manager.get_seed_by_time()
    return {"char": generators.generate_char(seed)}

@router.get("/random-integer")
async def nondet_integer(min_val: int = -2147483647, max_val: int = 2147483647):
    seed = seed_manager.get_seed_by_time()
    return {"integer": generators.generate_integer(seed, min_val, max_val)}

@router.get("/random-float")
async def det_float(min_val: float = -2147483647.0, max_val: float = 2147483647.0):
    seed = seed_manager.get_seed_by_time()
    return {"float": generators.generate_float(seed, min_val, max_val)}

@router.get("/random-hash")
async def nondet_hash(algorithm: str = "sha256"):
    try:
        seed = seed_manager.get_seed_by_time()
        return {"hash": generators.generate_hash(seed, algorithm)}
    except ValueError:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")

@router.get("/random-bytes")
async def nondet_bytes(length: int = 16):
    seed = seed_manager.get_seed_by_time()
    return {"bytes": generators.generate_bytes(seed, length)}

@router.get("/random-timestamp")
async def nondet_timestamp(days: int = 365):
    seed = seed_manager.get_seed_by_time()
    return {"timestamp": generators.generate_timestamp(seed, days)}

@router.get("/random-color")
async def nondet_color():
    seed = seed_manager.get_seed_by_time()
    return {"color": generators.generate_color(seed)}

@router.get("/random-uuid")
async def nondet_uuid():
    seed = seed_manager.get_seed_by_time()
    return {"uuid": generators.generate_uuid(seed)}

@router.get("/random-password")
async def nondet_password(length: int = 12):
    seed = seed_manager.get_seed_by_time()
    return {"password": generators.generate_password(seed, length)}

@router.get("/random-choice")
async def nondet_choice(items: str = ""):
    seed = seed_manager.get_seed_by_time()
    return {"choice": generators.random_choice(seed, items)}

@router.get("/random-ipv4")
async def nondet_ipv4():
    seed = seed_manager.get_seed_by_time()
    return {"ipv4": generators.generate_ipv4(seed)}

@router.get("/random-coords")
async def det_coords():
    seed = seed_manager.get_seed_by_time()
    return {"coords": generators.generate_coords(seed)}
