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