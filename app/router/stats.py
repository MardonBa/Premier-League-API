from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
import math
from utils.stats import get_stats, get_all_time_stats

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

@router.get("/all_time/clubs/{stat_type}")
async def get_all_time_club_stats(stat_type: str, top_n: int | None = 10, scraper: PlaywrightService = Depends(get_scraper)):
    top_n = min(top_n, 10)
    return await get_all_time_stats(scraper, 'club', stat_type, top_n)

@router.get("/all_time/players/{stat_type}")
async def get_all_time_player_stats(stat_type: str, top_n: int | None = 10, scraper: PlaywrightService = Depends(get_scraper)):
    top_n = min(top_n, 10)
    print(top_n)
    return await get_all_time_stats(scraper, 'player', stat_type, top_n)