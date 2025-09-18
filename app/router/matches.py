from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService

router = APIRouter(
    prefix="/matches",
    tags=["matches"],
)

@router.get("/")
async def get_all_matches(scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/matchweek/{week_number}")
async def get_matches_by_week(week_number: int, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{club}")
async def get_matches_by_club(club: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{club}/{competition}")
async def get_matches_by_club_and_competition(club: str, competition: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/past/{club}/{matchweek}")
async def get_past_matches_by_club_and_week(club: str, matchweek: int, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/upcoming/{club}/{matchweek}")
async def get_upcoming_matches_by_club_and_week(club: str, matchweek: int, scraper: PlaywrightService = Depends(get_scraper)):
    pass