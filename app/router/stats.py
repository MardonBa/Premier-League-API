from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
import math
from utils.stats import get_stats

router = APIRouter(
    prefix="/stats",
    tags=["stats"],
)

@router.get("/club-rankings/{stat_type}")
async def get_club_stats(stat_type: str, top_n: int | None = None, scraper: PlaywrightService = Depends(get_scraper)):
    return await get_stats(scraper, 'clubs', stat_type, top_n)

@router.get("/player-rankings/{stat_type}")
async def get_player_stats(stat_type: str, top_n: int | None = None, scraper: PlaywrightService = Depends(get_scraper)):
    return await get_stats(scraper, 'players', stat_type, top_n)

@router.get("/club/all_time/{stat_type}")
async def get_all_time_club_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/players/all_time/{stat_type}")
async def get_all_time_player_stats(stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass