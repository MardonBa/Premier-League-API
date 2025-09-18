from services.playwright_service import PlaywrightService

scraper = PlaywrightService(root_url="https://www.premierleague.com/")

async def init_scraper():
    await scraper.init()

async def close_scraper():
    await scraper.close()