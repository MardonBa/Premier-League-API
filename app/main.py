from fastapi import FastAPI
from .router import clubs, matches, players, stats, table
from app.core import init_scraper, close_scraper

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_scraper()

@app.on_event("shutdown")
async def shutdown_event():
    await close_scraper()

app.include_router(table.router)
app.include_router(clubs.router)
app.include_router(players.router)
app.include_router(matches.router)
app.include_router(stats.router)
