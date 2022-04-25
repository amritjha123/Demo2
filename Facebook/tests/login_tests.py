from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class TestLogin(unittest.TestCase):


    @pytest.mark.run(order=2)
    def test_validlogin(self):

        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("amritjhaworks@gmail.com", "passtold123!@#")
        result = lp.verifyLoginSuccessful()
        assert result == True
        driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        baseUrl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("amritjhaworks@gmail.com", "passtold123")
        result = lp.verifyLoginFailed()
        assert result == True
        driver.quit()

