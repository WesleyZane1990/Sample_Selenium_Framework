import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from common.project_utils import get_user_name, get_password
import os
import time

def test_sign_in(browser):

    homepage = LoginPage(browser).login(get_user_name(), get_password())
    time.sleep(5)

    assert homepage.is_app_logo_visible()

def test_sign_out(browser):

    homepage = LoginPage(browser).login(get_user_name(), get_password())
    time.sleep(5)

    assert homepage.is_app_logo_visible()

    login_page = HomePage(browser).sign_out()
    time.sleep(5)

    assert login_page.get_username_field() == ""
    assert login_page.get_password_field() == ""
