from fastapi import APIRouter, Depends
from .deps import get_scraper
from services.playwright_service import PlaywrightService

router = APIRouter(
    prefix="/clubs",
    tags=["clubs"],
)

async def get_players_by_position(scraper, club):
    page = await scraper.goto(f"/en/clubs/3/{club}/squad")
    row_locator = page.locator("div.club-profile__squad-container")
    await row_locator.wait_for(timeout=5000)
    sections = await row_locator.all_inner_texts()
    sections = [section.split("\n") for section in sections][0]
    counter = 0
    players = {'players': []}
    i = 0
    while i < len(sections):
        if sections[i] in {'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'}: ## skip the headings
            i += 1
            continue
        players['players'].append({
            'name': sections[i],
            'number': sections[i+1],
            'position': sections[i+2],
        })
        i += 3
    return players
            
        


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

@router.get("/{name}/{stat_type}")
async def get_club_stats(name: str, stat_type: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass

@router.get("/{name}/{stat_type}/{state_name}")
async def get_club_sub_stats(name: str, stat_type: str, state_name: str, scraper: PlaywrightService = Depends(get_scraper)):
    pass
