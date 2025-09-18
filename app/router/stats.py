from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
)

@router.get("/club/{stat_type}")
async def get_club_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/players/{stat_type}")
async def get_player_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/club/all_time/{stat_type}")
async def get_all_time_club_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/players/all_time/{stat_type}")
async def get_all_time_player_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass