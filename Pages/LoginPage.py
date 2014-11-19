import time
from selenium import webdriver
from BasePageElement import *
print("LoginPage.py is loaded")

from BasePage import BasePage
from LocatorTypes import LocatorTypes

class LoginPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.submit_button = BasePageElement(LocatorTypes.CSS_SELECTOR, "div.form div.ok input", self._driver)

    #Page elements descriptions

    @property
    def username_field(self):
        return self._driver.find_element_by_css_selector("form#loginform div.form div.champ input[name = 'lusername']")

    @property
    def password_field(self):
        return self._driver.find_element_by_css_selector("form#loginform div.form div.champ input[name = 'lpassword']")


##    submit_button.locator = "div.form div.ok input"
##    submit_button.locator_type = "by css selector"
##    def submit_button(self):
##        #locator = "div.form div.ok input"
##        #locator_type = "by css selector"
##        element = self._driver.find_element_by_css_selector(submit_button.locator)
##        element.locator = locator
##        element.locator_type = locator_type
##        return element




    def error_message(self):
        locator = "p.pasgood"
        element = self._driver.find_element_by_css_selector(locator)
        element.locator = locator
        return element



    def navigate_to(self):
        self._driver.get("http://www.openforbeta.com/login")


    def click_on_submit_button(self):
        self.submit_button().click()

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.click_on_submit_button()



##def main():
##
##    driver = webdriver.Firefox()
##
##    login_page = LoginPage(driver)
##    login_page.navigate_to()
##
##    login_page.login("Hrundel", "Chupacabra")
##
##if __name__ == '__main__':
##    main()


