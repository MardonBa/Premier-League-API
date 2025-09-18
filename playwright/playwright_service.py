from playwright.async_api import async_playwright
from urllib.parse import urljoin

class PlaywrightService:
    def __init__(self, root_url: str):
        self.root_url = root_url
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    async def init(self):
        if not self.browser:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=True)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()

    async def goto(self, path: str):
        if not self.page:
            raise RuntimeError("Playwright not initialized. Call init() first.")
        url = urljoin(self.root_url, path)
        await self.page.goto(url, wait_until="domcontentloaded")
        return self.page

    async def close(self):
        if self.browser:
            await self.browser.close()
            await self.playwright.stop()
            self.browser = None
            self.context = None
            self.page = None