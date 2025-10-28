from fastapi import APIRouter, Depends
from .deps import get_scraper
from utils.table import parse_table

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

@router.get("/")
async def get_league_table(scraper = Depends(get_scraper)): ## returns an ordered list of team dicttionaries
    return await parse_table(scraper)

@router.get("/{team_name}")
async def get_team_table_info(team_name: str, scraper = Depends(get_scraper)): ## returns
    table = await parse_table(scraper)
    for team in table['table']:
        if team['team'].lower() == team_name.lower():
            return team
    return {"error": "Team not found"}