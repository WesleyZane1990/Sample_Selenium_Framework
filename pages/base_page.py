from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait3 = WebDriverWait(driver, timeout)