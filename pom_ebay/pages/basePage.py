class BasePage:
    def __init__(self, page):
        self.page = page

    def find_smart_element(self, locators):
        last_exception = None

        for locator in locators:
            try:
                element = self.page.locator(locator)
                if element.is_visible():
                    print(f"Success with element locator : {locator}")
                    return element
            except Exception as e:
                print(f"Failed with {locator}. Trying next fallback...")
                last_exception = e

        raise Exception(f"All locators failed. Last error: {last_exception}")

    def smart_click(self, locators_list):
        element = self.find_smart_element(locators_list)
        element.click()

    def smart_fill(self, locators_list, text):
        element = self.find_smart_element(locators_list)
        element.fill(str(text))
