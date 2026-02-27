import pytest
from playwright.sync_api import Browser, Page

from pom_ebay.pages.advanced_page import advancedPage
from pom_ebay.pages.welcome_page import welcomePage


@pytest.fixture(scope="function")
def setup_playwright(browser: Browser, browser_name: str):
    print(f"#### Starting test on browser: {browser_name} ####")
    with allure.step("Starting test"):

        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto("https://www.ebay.com/")

        yield page,context
        with allure.step("Teardown test"):

            page.close()
            context.close()
            print(f"#### Test end on {browser_name} ####")


import allure
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')  # Assuming you use the 'page' fixture
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )