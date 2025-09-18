from fastapi import APIRouter, Depends
from .deps import get_scraper

router = APIRouter(
    prefix="/players",
    tags=["players"],
)

@router.get("/{name}", scraper = Depends(get_scraper))
async def get_player_by_name(name: str):
    pass

@router.get("/{name}/club", scraper = Depends(get_scraper))
async def get_player_club(name: str):
    pass

@router.get("/{name}/position", scraper = Depends(get_scraper))
async def get_player_position(name: str):
    pass

@router.get("/{player}/nationality", scraper = Depends(get_scraper))
async def get_player_nationality(player: str):
    pass

@router.get("/{name}/age", scraper = Depends(get_scraper))
async def get_player_age(name: str):
    pass

@router.get("/{name}/stats/{stat_type}", scraper = Depends(get_scraper))
async def get_player_stats(name: str, stat_type: str):
    pass


@router.get("/{name}/stats/{stat_type}/{state_name}", scraper = Depends(get_scraper))
async def get_player_sub_stats(name: str, stat_type: str, state_name: str):
    pass

@router.get("/{name}/fpl_price", scraper = Depends(get_scraper))
async def get_player_fpl_price(name: str):
    pass

@router.get("/{name}/fpl_points", scraper = Depends(get_scraper))
async def get_player_fpl_points(name: str):
    pass

@router.get("/{name}/fpl_points_by_week", scraper = Depends(get_scraper))
async def get_player_fpl_points_by_week(name: str):
    pass