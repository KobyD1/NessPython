pytest --browser chromium --browser firefox -n auto




scoop install allure
running the test
 python -m pytest --alluredir=allure-results
watching allure
allure serve allure-results