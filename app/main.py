from fastapi import FastAPI
from .router import clubs, matches, players, stats, table
from playwright.playwright_service import PlaywrightService

app = FastAPI()
scraper = PlaywrightService(root_url="https://www.premierleague.com/")

@app.on_event("startup")
async def startup_event():
    await scraper.init()

@app.on_event("shutdown")
async def shutdown_event():
    await scraper.close()

app.include_router(table.router)
