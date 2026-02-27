

1 . in order to run parallel with allure and screen capture in case of failure run :

python -m pytest --browser chromium --browser firefox -n auto --alluredir=allure-results --screenshot only-on-failure


2. in order to watch allure result run :
allure serve allure-results

3. to install enviroment run in project root :
pip install -r .\requirements_playwright
scoop install allure (sometimes allure can not installed by pip )

4. architecture
the project split to several  main parts
4.1 pages - for page objects per page
include base page with smart fill and smart click implement
smart fill and smart click did not used allways
=> in case of element define as user experiance (e.g by text ) -the test should failed in any case of user experianced changed

4.2 tests - for test file and conftest
4.3 images  -all screen capture (saved at dynamic method )
4.4 allure-results - json for allure run
in addition :
utils - for utils
globals - for globals parameters
req. - for needed modules
pytest.ini - init files for pytest (not in use )

