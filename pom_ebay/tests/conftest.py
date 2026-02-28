from datetime import datetime

import pytest
import allure
from playwright.sync_api import Browser

from pom_ebay.globals import URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        fixture_value = item.funcargs.get("setup_playwright")

        if fixture_value:
            page = fixture_value[0]

            screenshot = page.screenshot()
            timestamp = datetime.now().strftime("%d-%H-%M-%S")

            allure.attach(
                screenshot,
                name=f"Failure_screenshot_{timestamp}",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="function")
def setup_playwright(browser: Browser, browser_name: str):
    print(f"#### Starting test on browser: {browser_name} ####")

    with allure.step("Starting test"):
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto(URL)

        yield page, context

    with allure.step("Teardown test"):
        page.close()
        context.close()
        print(f"#### Test end on {browser_name} ####")
