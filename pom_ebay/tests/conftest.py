import pytest
from playwright.sync_api import Browser, Page

from pom_ebay.pages.advanced_page import advancedPage
from pom_ebay.pages.welcome_page import welcomePage


@pytest.fixture(scope="function")
def setup_playwright(browser: Browser, browser_name: str):
    print(f"#### Starting test on browser: {browser_name} ####")

    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto("https://www.ebay.com/")





    yield page,context

    page.close()
    context.close()
    print(f"#### Test end on {browser_name} ####")