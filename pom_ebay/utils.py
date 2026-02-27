import allure


class Utils():

    def print_urls_to_consol(self,urls):
        with allure.step(f" URL's for products  ") :

            for url in urls:
                print (f"url for product {url} ")