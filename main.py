from fastapi import FastAPI
from routers import det_routers, nondet_routers

app = FastAPI()
app.include_router(det_routers.router)
app.include_router(nondet_routers.router)
