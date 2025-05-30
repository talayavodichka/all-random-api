import os
from datetime import datetime

def get_seed_by_time() -> str:
    return f"{datetime.now().timestamp()}-{os.urandom(16).hex()}"
