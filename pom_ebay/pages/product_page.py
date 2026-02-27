

from pom_ebay.pages.basePage import BasePage
from pom_ebay.pages.locators import advPageLocators, productPageLocators


class productPage():

    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    def navigate_to_welcome_page(self):
        self.page.close()

    def get_price(self):
        text = self.page.get_by_text(productPageLocators.PRICE_TEXT).inner_text()
        price_text = text.split(" ")[1]
        print (f"Price in ILS found the price is {price_text} ILS")
        return float(price_text)


    def set_product_details(self):
        print (f"Trying to set product details by drop down")
        self.page.wait_for_selector(productPageLocators.IMAGE_ID)
        drop_down_elements=self.page.get_by_text(productPageLocators.DROP_DOWN_TEXT).all()
        drop_down_amount = len(drop_down_elements) # handling cases of inconsist amount of drop down at diffrent  products
        for i in range(drop_down_amount):
            element =self.page.get_by_text(productPageLocators.DROP_DOWN_TEXT).all()[0]
            element.click()
            element.press("ArrowDown")
            element.press("Enter")

    def add_to_cart(self):
        # bypass , clicking on it navigate to identity page
        self.page.get_by_text("Add to cart").click()
        self.page.get_by_text("See in cart").all()[1].click()







