from fastapi import FastAPI, HTTPException, Depends, Request, Response
from .router import clubs, matches, players, stats, table
from app.core import init_scraper, close_scraper
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from math import ceil
from contextlib import asynccontextmanager

REDIS_URL = "redis://127.0.0.1:6379"

async def service_name_identifier(req: Request):
    service = req.headers.get("Service-Name")
    return service or req.client

async def custom_callback(req: Request, res: Response, pexpire: int):
    expire = ceil(pexpire / 1000)

    raise HTTPException(
        status_code=429,
        detail=f"Too Many Requests. Retry after {expire} seconds.",
        headers={"Retry-After": str(expire)},
    )


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis_connection = redis.from_url(REDIS_URL, encoding="UTF-8")
    await FastAPILimiter.init(redis=redis_connection, 
                              identifier=service_name_identifier, 
                              http_callback=custom_callback)
    yield
    await FastAPILimiter.close()


app = FastAPI(lifespan=lifespan, dependencies=[Depends(RateLimiter(times=1, seconds=5))])

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
