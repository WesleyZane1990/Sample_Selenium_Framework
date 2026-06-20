from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC

from pages.base_page import BasePage
from pages.home_page import HomePage

class LoginPage(BasePage):

    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo']")
    USERNAME_FIELD = (By.XPATH, "//*[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//*[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")
    ERROR_MESSAGE_TEXT = "Epic sadface: Username and password do not match any user in this service"

    def login(self, username, password):

        self.wait3.until(EC.visibility_of_element_located(self.LOGIN_LOGO))
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.wait3.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()

        return HomePage(self.driver)

    def get_username_field(self):
        return self.wait3.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("value")

    def get_error_message(self):
        return self.wait3.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text