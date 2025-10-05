from playwright.async_api import async_playwright
from urllib.parse import urljoin

class PlaywrightService:
    def __init__(self, root_url: str):
        self.root_url = root_url
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.initial_render = True
        self.headless = True

    async def init(self):
        if not self.browser:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=self.headless)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()

    async def goto(self, path: str):
        if not self.page:
            raise RuntimeError("Playwright not initialized. Call init() first.")
        url = urljoin(self.root_url, path)
        await self.page.goto(url, wait_until="domcontentloaded")
        
        if self.initial_render and not self.headless:
            cookie_button = self.page.locator("button:has-text('Accept All Cookies')")
            await cookie_button.click()
            self.initial_render = False
        return self.page

    async def close(self):
        if self.browser:
            await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
            self.browser = None
            self.context = None
            self.page = None