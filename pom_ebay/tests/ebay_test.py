import allure
from playwright.sync_api import expect

from pom_ebay.globals import ITEM_TO_FIND, MIN_PRICE, MAX_PRICE, ITEMS_QUANTITY, MAX_BUDGET
from pom_ebay.pages.advanced_page import advancedPage
from pom_ebay.pages.product_page import productPage
from pom_ebay.pages.welcome_page import welcomePage


class TesteBay():


    def test_search_items_under_price(self,setup_playwright):
        allure.dynamic.title(f"E2E Test for search {ITEM_TO_FIND} in at least {ITEMS_QUANTITY} times- eBay")
        page,context  = setup_playwright
        welcome_page = welcomePage(page,context)
        adv_page= advancedPage(page)
        # welcome_page.login_with_user_password("abc@gmail.com","123456")
        welcome_page.click_on_popup_if_exist()
        assert 4 == 5
        welcome_page.click_on_adv_link()

        adv_page.search_for_item_by_price(ITEM_TO_FIND,MIN_PRICE,MAX_PRICE)
        results_elements = welcome_page.get_items_prices_by_quantity(ITEMS_QUANTITY)
        summery = 0
        for element in results_elements:
            new_tab = welcome_page.click_on_result_image(element)
            product_page = productPage(new_tab)
            product_page.set_product_details()
            price =product_page.get_price()
            summery += price
            product_page.navigate_to_welcome_page()
        print (f"total price is {summery}")
        assert summery<=MAX_BUDGET,f"summery is more than price at  to {MAX_PRICE}"
        assert len(results_elements)>=ITEMS_QUANTITY,f"low amount of items found "






