from fastapi import APIRouter, Depends
from .deps import get_scraper
import asyncio

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

async def parse_table(scraper = Depends(get_scraper)):
    page = await scraper.goto("/en/tables?competition=8&season=2025&round=L_1&matchweek=-1&ha=-1")

    rows_locator = page.locator("tbody tr .standings-row__container")
    await rows_locator.first.wait_for(timeout=30000)
    rows = await rows_locator.all_inner_texts()
    table = []
    for row in rows:
        row_data = row.split("\n")
        team_data = {
            'position': row_data[0],
            'team': row_data[1],
            'played': row_data[2],
            'won': row_data[3],
            'drawn': row_data[4],
            'lost': row_data[5],
            'goals_for': row_data[6],
            'goals_against': row_data[7],
            'goal_difference': row_data[8],
            'points': row_data[9],
        }
        table.append(team_data)
    return {'table': table}

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