from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
from utils.clubs import get_players_by_position, get_all_club_stats, format_stats

router = APIRouter(
    prefix="/clubs",
    tags=["clubs"],
)

@router.get("/{name}/players")
async def get_club_players(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    return await get_players_by_position(scraper, name)


@router.get("/{name}/players/{position}")
async def get_club_players_by_position(name: str, position: str, scraper: PlaywrightService = Depends(get_scraper)):
    players = await get_players_by_position(scraper, name)
    filtered_players = {'players': []}
    for player in players['players']:
        if player['position'].lower() == position.lower():
            filtered_players['players'].append(player)
    return filtered_players

@router.get("/{name}/stats")
async def get_club_overall_stats(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    stats = await get_all_club_stats(scraper, name)
    return format_stats(stats)

@router.get("/{name}/stats/{stat_type}")
async def get_club_stats(name: str, stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    stats = await get_all_club_stats(scraper, name)
    return format_stats(stats)[stat_type.title()]

@router.get("/{name}/stats/{stat_type}/{stat_name}")
async def get_club_sub_stats(name: str, stat_type: str, stat_name: str, scraper: PlaywrightService = Depends(get_scraper)):
    stats = await get_all_club_stats(scraper, name)
    return {str(stat_name.title()): format_stats(stats)[stat_type.title()][stat_name.title()]}
