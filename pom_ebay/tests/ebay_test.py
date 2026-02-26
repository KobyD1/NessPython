from playwright.sync_api import expect

from pom_ebay.globals import ITEM_TO_FIND, MIN_PRICE, MAX_PRICE
from pom_ebay.pages.advanced_page import advancedPage
from pom_ebay.pages.welcome_page import welcomePage


class TesteBay():


    def test_search_items_under_price(self, setup_playwright):

        page  = setup_playwright
        welcome_test = welcomePage(page)
        adv_page= advancedPage(page)
        welcome_test.click_on_adv_link()

        adv_page.search_for_item_by_price(ITEM_TO_FIND,MIN_PRICE,MAX_PRICE)



        expect(page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch","page URL is not as expected after login"



