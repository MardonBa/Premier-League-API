from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
from utils.players import get_player_info

router = APIRouter(
    prefix="/players",
    tags=["players"],
)

@router.get("/{name}")
async def get_player_by_name(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    await get_player_info(scraper, name)
    return 'poopy butthead'

@router.get("/{name}/club")
async def get_player_club(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/position")
async def get_player_position(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{player}/nationality")
async def get_player_nationality(player: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/age")
async def get_player_age(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/stats")
async def get_player_stats(name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

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