from fastapi import FastAPI
from .router import clubs, matches, players, stats, table

app = FastAPI()

app.include_router(table.router)
