#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      _Intel_
#
# Created:     31.10.2014
# Copyright:   (c) _Intel_ 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
from selenium import webdriver
from BasePageElement import *
print("MasterPage.py is loaded")

from BasePage import BasePage
from LocatorTypes import LocatorTypes
from selenium.webdriver.common.action_chains import ActionChains


class MasterPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.navigation_dropdown = BasePageElement(LocatorTypes.XPATH, "//a[contains(text(), 'qtest')]", self._driver)
        self.navigation_item = BasePageElement(LocatorTypes.XPATH, "//a[text() = '%']", self._driver)

    def click_on_logout(self):
        action = ActionChains(self._driver)
        action.move_to_element(self.navigation_dropdown())
        action.click(self.navigation_item(["Logout"]))
        action.perform()