python -m pytest --browser chromium --browser firefox -n auto --alluredir=allure-results --screenshot only-on-failure --video retain-on-failure --output=test-results


scoop install allure
running the test
 python -m pytest --alluredir=allure-results
watching allure
allure serve allure-results