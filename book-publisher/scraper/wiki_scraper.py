import sys
import os

# Add the config directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../config')))

from config.playwright_config import get_browser

class WikiScraper:
    def __init__(self, url):
        self.url = url

    def fetch_text_and_screenshot(self, out_txt, out_png):
        browser, playwright = get_browser()
        page = browser.new_page()
        page.goto(self.url)
        page.screenshot(path=out_png, full_page=True)
        content = page.inner_text("body")
        with open(out_txt, "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
        playwright.stop()
        return content
