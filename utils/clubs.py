
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