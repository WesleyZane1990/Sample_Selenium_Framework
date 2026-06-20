import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.project_utils import get_browser, get_url


@pytest.fixture(scope="function")
def browser():
    get_browser()

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    print("Browser is opening")

    driver=webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)

    print("Getting Page")
    driver.get(get_url())

    yield driver
    print("\nBrowser is closed")
    driver.close()
    driver.quit()