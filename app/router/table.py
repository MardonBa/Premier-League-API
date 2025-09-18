from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

@router.get("/")
async def get_league_table(scraper = Depends(get_scraper)):
    return {"message": "League table data"}