from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger(logging.DEBUG)

    _email_field = "//input[@name='email']"
    _password_field = "//input[@name='pass']"
    _login_button = "//button[@name='login']"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[@class='_1vp5']")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='_9ay7']")
        return result