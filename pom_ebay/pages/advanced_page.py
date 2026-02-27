from pom_ebay.pages.basePage import BasePage
from pom_ebay.pages.locators import advPageLocators


class advancedPage():

    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)



    def search_for_item_by_price(self, item:str,min_price:int,max_price:int):
        print (f"Trying to search between {min_price} and {max_price}")
        self.base_page.smart_fill(advPageLocators.min_price_locators,min_price)
        self.base_page.smart_fill(advPageLocators.max_price_locators,max_price)
        self.base_page.smart_fill(advPageLocators.search_menu_locators,item)
        self.page.keyboard.press("Enter")




