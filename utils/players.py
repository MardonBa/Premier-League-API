import time

async def search_for_player(scraper, player_name):
    page = await scraper.goto("/en/players?competition=8&season=2025")
    search_locator = page.locator('div.text-input.text-input--text.text-input--default.text-input--search label input')
    await search_locator.fill(player_name)
    time.sleep(1) ## wait for the page to update what players are displayed on the screen
    return page

async def get_player_info(scraper, player_name):
    page = await search_for_player(scraper, player_name)
    table_locator = page.locator('table tbody tr.player-listings-row').first
    await table_locator.wait_for()
    text = await table_locator.inner_text()
    text_list = [t.strip() for t in text.split("\t")]
    text_list = [t for t in text_list if t != '']
    