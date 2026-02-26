from playwright.sync_api import expect

from pom_ebay.pages.locators import welcomePageLocators


# from pom_ebay.pages.smart_locators import advPageLocators


class welcomePage():

    def __init__(self, page):
        self.page = page

    def click_on_adv_link(self):
        adv_link = self.page.get_by_text(welcomePageLocators.adv_link_text)
        adv_link.click()
        expect(self.page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")

    def click_on_login(self):
        login = self.page.get_by_text("Login")
        login.click()
