from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
)

@router.get("/club/{stat_type}", scraper = Depends(get_scraper))
async def get_club_stats(stat_type: str):
    pass

@router.get("/players/{stat_type}", scraper = Depends(get_scraper))
async def get_player_stats(stat_type: str):
    pass

@router.get("/club/all_time/{stat_type}", scraper = Depends(get_scraper))
async def get_all_time_club_stats(stat_type: str):
    pass

@router.get("/players/all_time/{stat_type}", scraper = Depends(get_scraper))
async def get_all_time_player_stats(stat_type: str):
    pass