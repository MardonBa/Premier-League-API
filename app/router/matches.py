from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/matches",
    tags=["matches"],
)

@router.get("/", scraper = Depends(get_scraper))
async def get_all_matches():
    pass

@router.get("/matchweek/{week_number}", scraper = Depends(get_scraper))
async def get_matches_by_week(week_number: int):
    pass

@router.get("/{club}", scraper = Depends(get_scraper))
async def get_matches_by_club(club: str):
    pass

@router.get("/{club}/{competition}", scraper = Depends(get_scraper))
async def get_matches_by_club_and_competition(club: str, competition: str):
    pass

@router.get("/past/{club}/{matchweek}", scraper = Depends(get_scraper))
async def get_past_matches_by_club_and_week(club: str, matchweek: int):
    pass

@router.get("/upcoming/{club}/{matchweek}", scraper = Depends(get_scraper))
async def get_upcoming_matches_by_club_and_week(club: str, matchweek: int):
    pass