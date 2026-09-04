import time

from pages.home_page import HomePage
from pages.login_page import LoginPage
from common.project_utils import get_user_name, get_password
import os
import pytest

def test_sign_in(browser):

    homepage = LoginPage(browser).login(get_user_name(), get_password())

    assert homepage.is_app_logo_visible()

def test_sign_out(browser):

    homepage = LoginPage(browser).login(get_user_name(), get_password())

    assert homepage.is_app_logo_visible()

    login_page = HomePage(browser).sign_out()

    assert login_page.get_username_field() == ""
    assert login_page.get_password_field() == ""


def test_sign_in_with_false_credentials(browser):

    LoginPage(browser).login(os.getenv("NO_USERNAME"), os.getenv("NO_PASSWORD"))

    assert LoginPage(browser).is_error_message_visible()

    text = LoginPage(browser).get_error_message()

    assert text == LoginPage.ERROR_MESSAGE_TEXT