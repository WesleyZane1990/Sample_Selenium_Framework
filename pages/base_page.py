from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
import pages
import time

class BasePage:

    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait3 = WebDriverWait(driver, timeout)