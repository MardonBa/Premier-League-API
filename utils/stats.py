async def select_and_click_item(page, selector, n: int | None = None, element_text: int | None = None):
    if n != None:
        locator = page.locator(selector).nth(n)
    elif element_text != None:
        locator = page.locator(selector).get_by_text(element_text)
    else:
        locator = page.locator(selector)
    await locator.wait_for()
    await locator.click()

async def get_stats(scraper, category, stat_type, top_n):
    top_n = 10 if top_n == None else top_n
    num_page_changes = math.floor((top_n-1) / 10)

    data = []
    page = await scraper.goto(f'/en/stats/top/{category}?statMetric={stat_type}&season=2025')

    if stat_type != 'goals':
        await select_and_click_item(page, 'button.chip', n=1) ## open the dropdown
        await select_and_click_item(page, 'label.input-button__label', element_text=stat_type) ## select the stat
        await select_and_click_item(page, 'span.button__label', element_text='Save')

    for i in range(num_page_changes+1):
        data_locator = page.locator('tbody tr td.stats-table__stat-wrapper')
        await data_locator.first.wait_for(timeout=30000)
        cur_data = await data_locator.all_inner_texts()
        cur_data = [d.split("\n") for d in cur_data]
        cur_data = [{
            'position': int(d[0]),
            f'{category}_name': d[1],
            f'{stat_type}': int(d[-1]) if d[-1].isdigit() else 0
        } for d in cur_data]
        data.extend(cur_data)
        locator = page.locator('button.button__icon-right').nth(2)
        await locator.wait_for()
        await locator.click()
    return {'stats': data[:top_n]}

async def get_all_time_stats(scraper, category, stat_type, top_n):
    page = await scraper.goto(f'/en/stats/all-time')
    section_locator = page.locator("div.row").nth(0 if category == 'player' else 1)
    await section_locator.wait_for()
    while True:
        section_data = await section_locator.all_inner_texts()
        section_data = section_data[0].split("\n")
        if not '\u200c' in section_data: ## fixes issue that comes up sporadically
            break
    idx = section_data.index(stat_type.title())
    desired_data = section_data[idx+1:idx+31]
    data_obj = {stat_type: []}
    for i in range(0, len(desired_data), 3):
        data_obj[stat_type].append({
            category: desired_data[i+1],
            'count': desired_data[i+2]
        })
        top_n -= 1
        if top_n == 0: break ## make sure we only get the top n (up to 10) players
    return data_obj