import time
from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage

class HomePage(BasePage):
    USERNAME_FIELD = (By.XPATH, "//*[@id='user-name']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")

    def is_app_logo_visible(self):
        return self.wait3.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='app_logo']"))).is_displayed()

    def show_dropdown_menu(self):
        menu_icon = self.wait3.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        ActionChains(self.driver).move_to_element(menu_icon).perform()

        return self

    def click_dropdown_menu(self):
        dropdown_menu_element = "//*[@id='react-burger-menu-btn']"
        dropdown_menu_clickable = self.wait3.until(EC.element_to_be_clickable((By.XPATH, dropdown_menu_element)))

        try:
            dropdown_menu_clickable.click()
        except StaleElementReferenceException:
            self.wait3.until(EC.element_to_be_clickable((By.XPATH, dropdown_menu_element)))

        return self


    def click_sign_out_element(self):
        sign_out_element = "//*[@id='logout_sidebar_link']"
        sign_out_element_visible = self.wait3.until(EC.visibility_of_element_located((By.XPATH, sign_out_element)))
        ActionChains(self.driver).move_to_element(sign_out_element_visible).perform()
        sign_out_element_visible.click()

        return self

    def sign_out(self):
        return self.show_dropdown_menu().click_dropdown_menu().click_sign_out_element()

    def get_username_field(self):
        return self.wait3.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("value")