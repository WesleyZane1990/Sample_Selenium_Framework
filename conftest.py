import pytest
from selenium import webdriver

from common.project_utils import get_browser, get_options, get_url

@pytest.fixture(scope="function")
def browser():
    get_browser()

    options = webdriver.ChromeOptions()
    for option in get_options():
        options.add_argument(option)
    print("Browser is opening")

    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    print("Getting Page")
    driver.get(get_url())

    yield driver
    print("\nBrowser is closed")
    driver.close()
    driver.quit()