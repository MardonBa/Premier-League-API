from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/clubs",
    tags=["clubs"],
)

@router.get("/{name}/table_info", scraper = Depends(get_scraper))
async def get_club_table_info(name: str):
    pass

@router.get("/{name}/players", scraper = Depends(get_scraper))
async def get_club_players(name: str):
    pass

@router.get("/{name}/players/{position}", scraper = Depends(get_scraper))
async def get_club_players_by_position(name: str, position: str):
    pass

@router.get("/{name}/{stat_type}", scraper = Depends(get_scraper))
async def get_club_stats(name: str, stat_type: str):
    pass

@router.get("/{name}/{stat_type}/{state_name}", scraper = Depends(get_scraper))
async def get_club_sub_stats(name: str, stat_type: str, state_name: str):
    pass