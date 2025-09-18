from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

@router.get("/", scraper = Depends(get_scraper))
async def get_league_table():
    return {"message": "League table data"}