import allure
from playwright.sync_api import expect

from pom_ebay.pages.locators import welcomePageLocators


class welcomePage():

    def __init__(self, page, context):
        self.page = page
        self.context = context

    def click_on_adv_link(self):
        with allure.step("Clicking Adv. button and verify for success "):
            adv_link = self.page.get_by_text(welcomePageLocators.adv_link_text)
            adv_link.click()
            expect(self.page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")
            print(f"Adv. link is {self.page.url}")

    def get_items_prices_by_quantity(self, quantity=1):
        with allure.step(f"Getting items prices {quantity} products "):

            self.page.locator(welcomePageLocators.found_text_locator).wait_for(state="visible")
            elements = self.page.locator(welcomePageLocators.products_elements).all()

            if len(elements) > quantity:
                return elements[2:quantity + 2]  # added due to 2 elements shift
            else:
                return []

    def click_on_popup_if_exist(self):
        try:
            with allure.step("Clicking on popup button if appears"):
                button = self.page.locator("button.btn.submit-button.btn--primary btn--fluid")
                button.click()
        except:
            print("Pop up did not appears ")
            pass

    def click_on_result_image(self, image_element):
        with allure.step(f"Clicking on product image as a results of search "):
            print("Clicking on product image as a results of search")
            with self.context.expect_page() as new_page_info:
                image_element.click()

            new_tab = new_page_info.value

            new_tab.bring_to_front()
            return new_tab

    def login_with_user_password(self, user_text, password_text="123456"):
        print(f"Trying to login with user {user_text}, temporary blocked due security issue ")
        user_menu = self.page.get_by_role("link", name="Sign in").click()
        user_menu.fill(user_text)
