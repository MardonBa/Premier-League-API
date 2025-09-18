from fastapi import APIRouter, Depends
from .deps import get_scraper
import asyncio

router = APIRouter(
    prefix="/table",
    tags=["table"],
)

@router.get("/")
async def get_league_table(scraper = Depends(get_scraper)): ## returns an ordered list of team dicttionaries
        ## navigate to the league table page
    page = await scraper.goto("/en/tables?competition=8&season=2025&round=L_1&matchweek=-1&ha=-1")
    table = await page.inner_html(".standings-table")
    rows = await page.query_selector_all("tbody tr .standings-row__container")
    print(type(rows))
    table = []
    print(len(rows))
    print((await rows[0].inner_text()).split("\n"))
    for row in rows:
        row_data = (await row.inner_text()).split("\n")
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
