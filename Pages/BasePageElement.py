#-------------------------------------------------------------------------------
# Copyright 2014 Aleksey Litvinov litvinov.aleks@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------

from LocatorTypes import LocatorTypes
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BasePageElement:

    def __init__(self, locator_type, locator, driver, name = ""):
        self.locator_type = locator_type
        self.locator = locator
        self._driver = driver


    def __call__(self, injections = []):
        if injections == []:
            return BasePageElement.get_static_element(self.locator_type, self.locator, self._driver)
        else:

            return BasePageElement.get_dynamic_element(self.locator_type, self.locator, self._driver, injections)


    @staticmethod
    def get_static_element(locator_type, locator, driver):
        if(locator_type == LocatorTypes.ID):
            return driver.find_element_by_id(locator)
        elif(locator_type == LocatorTypes.XPATH):
            return driver.find_element_by_xpath(locator)
        elif(locator_type == LocatorTypes.LINK_TEXT):
            return driver.find_element_by_link_text(locator)
        elif(locator_type == LocatorTypes.PARTIAL_LINK_TEXT):
            return driver.find_element_by_partial_link_text(locator)
        elif(locator_type == LocatorTypes.NAME):
            return driver.find_element_by_name(locator)
        elif(locator_type == LocatorTypes.TAG_NAME):
            return driver.find_element_by_tag_name(locator)
        elif(locator_type == LocatorTypes.CLASS_NAME):
            return driver.find_element_by_class_name(locator)
        elif(locator_type == LocatorTypes.CSS_SELECTOR):
            return driver.find_element_by_css_selector(locator)


    @staticmethod
    def get_dynamic_element(locator_type, locator, driver, injections = []):
        locator = BasePageElement.inject_values(locator, injections)
        return BasePageElement.get_static_element(locator_type, locator, driver)

    @staticmethod
    def inject_values(locator, injections):
        locator_with_injection = locator
        for injection in injections:
            locator_with_injection = locator_with_injection.replace('%', injection, 1)
        return locator_with_injection
