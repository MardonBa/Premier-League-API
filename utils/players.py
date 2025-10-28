import time

async def search_for_player(scraper, player_name):
    page = await scraper.goto("/en/players?competition=8&season=2025")
    search_locator = page.locator('div.text-input.text-input--text.text-input--default.text-input--search label input')
    await search_locator.fill(player_name)
    time.sleep(1) ## wait for the page to update what players are displayed on the screen
    table_locator = page.locator('table tbody tr.player-listings-row').first
    await table_locator.wait_for()
    return table_locator, page

async def navigate_to_player_page(locator, name):
    locator = locator.get_by_text(name);
    await locator.click()

async def create_player_dict(locator):
    text = await locator.inner_text()
    text_list = [t.strip() for t in text.split("\t")]
    text_list = [t for t in text_list if t != '']
    player_dict = {
        'name': '',
        'club': '',
        'position': '',
        'nationality': ''
    }
    if len(text_list) == 5:
        player_dict['name'] = text_list[0]
        player_dict['club'] = text_list[1]
        player_dict['position'] = text_list[2]
        player_dict['nationality'] = text_list[3]
    else:
        player_dict['name'] = text_list[0]
        player_dict['club'] = 'No longer active'
        player_dict['position'] = text_list[1]
        player_dict['nationality'] = text_list[2]
    return player_dict

async def get_player_info(scraper, player_name):
    locator, _ = await search_for_player(scraper, player_name)
    return await create_player_dict(locator)

async def player_stats(scraper, player_name):
    table, page = await search_for_player(scraper, player_name)
    player_name = (await create_player_dict(table))['name']
    await navigate_to_player_page(table, player_name)
    url = page.url.replace('overview', 'stats')
    page = await scraper.goto(url)
    data_locator = page.locator('div.player-profile__panel')
    await data_locator.wait_for(timeout=30000)
    stats = await data_locator.all_inner_texts()
    print(stats)
    stats = stats[0].split("\n")
    print(stats)
    stats = [stat for stat in stats if stat != '']
    ## above gives us the text from selecting the year, we don't want any of that
    stats = stats[stats.index('Save')+1:]
    return stats