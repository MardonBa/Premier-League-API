from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
from utils.players import get_player_info, player_stats
from utils.utils import format_stats

router = APIRouter(
    prefix="/players",
    tags=["players"],
)

@router.get("/{name}")
async def get_player_by_name(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    return await get_player_info(scraper, name)

@router.get("/{name}/club")
async def get_player_club(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    return (await get_player_info(scraper, name))['club']

@router.get("/{name}/position")
async def get_player_position(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    return (await get_player_info(scraper, name))['position']

@router.get("/{name}/nationality")
async def get_player_nationality(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    return (await get_player_info(scraper, name))['nationality']

@router.get("/{name}/stats")
async def get_player_stats(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    stats =  await player_stats(scraper, name)
    return format_stats(stats)

@router.get("/{name}/stats/{stat_type}")
async def get_player_stats_by_type(name: str, stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/stats/{stat_type}/{state_name}")
async def get_player_sub_stats(name: str, stat_type: str, state_name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/career-history")
async def get_player_career_history(name, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/fpl_price")
async def get_player_fpl_price(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/fpl_points")
async def get_player_fpl_points(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/fpl_points_by_week")
async def get_player_fpl_points_by_week(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass