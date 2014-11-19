
#global import

import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import traceback


sys.path.append("./../Pages/")
sys.path.append("./../Automation/")

from Pages.LoginPage import LoginPage
from Pages.MasterPage import MasterPage
from Automation.WebVerificator import WebVerify
#from Automation.WebInitializator import *
from Automation.Logger import Logger
script_name = "../Reports/" + os.path.splitext(os.path.basename(__file__))[0]

#Here logger should be created and passed to all objects

registered_username = "qtest"
notregistered_username = "qqqtest"
valid_password = "123456"
invalid_password = "654321"
url_after_login_expected = "http://www.openforbeta.com/account"
error_password_not_entered = "Error: Password not entered."
error_username_not_entered = "Error: Username not entered."
error_user_not_registered = "Error: Register before submission."
error_wrong_combination = "Error: Wrong username/password combination."


def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = element.location['y']
    driver.execute_script('window.scrollTo(0, {0})'.format(y))


try:
    driver = webdriver.Firefox()

    logger = Logger(script_name)
    verify = WebVerify(logger, driver = driver)

    login_page = LoginPage(driver)
    master_page = MasterPage(driver)
##    login_page.navigate_to()
##
##    verify.isElementPresent(login_page.submit_button)
##
##    login_page.login("Hrundel", "Chupacabra")
##
##    verify.isElementPresent(login_page.error_message)

##qtest@test.net
##123456
##qtest


    #Navigate to login form.
    login_page.navigate_to()


    verify.is_attribute(login_page.submit_button, "type", "submit")

    #Enter already registered user. Do not check Remember Me check box.
    login_page.login(registered_username, valid_password)

    #Verify User logs to site
    verify.is_page_url(url_after_login_expected)
    verify.is_title("Open for Beta - My Account")

    adv_link = driver.find_element_by_link_text("Advertise")
    y = adv_link.location['y']
    driver.execute_script('window.scrollTo(0, {0})'.format(y))
    time.sleep(10)
    #Log out
    master_page.click_on_logout()

    #Verify User logs out the site


    #Fill in login form with valid Username and empty Password field.
    #Press Login button.
    login_page.login(registered_username, "")

    #Verify "Error: Password not entered." message is displayed.
    verify.is_element_has_text(login_page.error_message, error_password_not_entered)

    #Fill in login form with valid password (of registered user) and empty Username field.
    #Press Login button.
    login_page("", valid_password)

    #Verify Message about empty username is displayed.
    verify.is_element_has_text(login_page.error_message, error_username_not_entered)

    #Leave all fields empty on login form.
    #Press Login button.
    login_page.login("", "")

    #Verify "Error: Register before submission." message is displayed.
    verify.is_element_has_text(login_page.error_message, error_user_not_registered)

    #Fill in login form with valid Username and incorrect Password field.
    #Press Login button.
    login_page.login(registered_username, invalid_password)

    #Verify "Error: Wrong username/password combination." message is displayed.
    verify.is_element_has_text(login_page.error_message, error_wrong_combination)

    #Fill in login form with not-registered username and any Password field.
    #Press Login button.
    login_page.login(notregistered_username, valid_password)

    #Verify "Error: Wrong username/password combination." message is displayed.
    verify.is_element_has_text(login_page.error_message, error_wrong_combination)



##"Fill in login form with registered user and check Remember Me check box.
##Close browser and start it again."
##


##"Fill in login form with registered user and check Remember Me check box.
##Close tab with site and navigate to it again."
##


##"Fill in login form with registered user and DO NOT check Remember Me check box.
##Close browser and start it again."
##
##"Fill in login form with registered user and DO NOT check Remember Me check box.
##Close tab with site and navigate to it again."
















except Exception as e:
    #log unexpected errror here
    error_traceback = traceback.format_exc()
    logger.log(error_traceback)

finally:
    driver.quit()
    verify.print_footer()