
async def get_players_by_position(scraper, club):
    page = await scraper.goto(f"/en/clubs/3/{club}/squad")
    data_locator = page.locator("div.club-profile__squad-container")
    await data_locator.wait_for(timeout=5000)
    sections = await data_locator.all_inner_texts()
    sections = sections[0].split("\n")
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