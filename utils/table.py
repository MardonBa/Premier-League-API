async def parse_table(scraper):
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