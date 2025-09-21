from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService
from utils.clubs import get_players_by_position

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

async def get_all_club_stats(scraper, club):
    page = await scraper.goto(f"/en/clubs/3/{club}/stats");
    data_locator = page.locator("div.club-profile__stats")
    await data_locator.wait_for(timeout=30000)
    stats = await data_locator.all_inner_texts()
    stats = stats[0].split("\n")
    stats = [stat for stat in stats if stat != '']
    return stats

def format_stats(stats):
    stats_dict = {
        "General": {},
        "Attack": {},
        "Defence": {},
        "Possession": {},
        "Physical": {},
        "Discipline": {}
    }
    cur_obj = "General" ## changed once we encounter the next heading
    skip_cur = False
    for i in range(len(stats)):
        if skip_cur: ## skip the numbers
            skip_cur = False
            continue
        elif stats[i] in set(stats_dict.keys()):
            cur_obj = stats[i]
            continue
        stats_dict[cur_obj][stats[i]] = stats[i+1]
        skip_cur = True
    return stats_dict


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
