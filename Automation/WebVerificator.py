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

from Verificator import Verify

class WebVerify(Verify):

    def __init__(
            self,
            logger,
            is_enabled=True,
            test_delimeter='',
            locale="ru",
            is_console=False,
            global_continue=None,
            driver = None
    ):
        Verify.__init__(
            self,
            logger,
            is_enabled=True,
            test_delimeter='',
            locale="ru",
            is_console=False,
            global_continue=None
    )
        self._driver = driver

    def check_driver(self):
        if self._driver is None:
            raise Exception

    def is_element_present(self, element, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' is present."
            self.logger.log(message)
            try:
                element(injections)
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time = False)

    def is_element_not_present(self, element, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' is not present."
            self.logger.log(message)
            try:
                element(injections)
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if(stop):
                    raise AssertionError
            except:
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
        self.logger.log(self.test_delimeter * 80, with_time=False)


    def is_element_has_text(self, element, text, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' has '" + text + "' text."
            self.logger.log(message)
            try:
                if element(injections).text == text:
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time = False)


    def is_element_not_have_text(self, element, text, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' doesn't have '" + text + "' text."
            self.logger.log(message)
            try:
                if element(injections).text != text:
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_element_contains_text(self, element, text, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' contains '" + text + "' text."
            self.logger.log(message)
            try:
                if text in element(injections).text:
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_element_not_contain_text(self, element, text, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' contains '" + text + "' text."
            self.logger.log(message)
            try:
                if text not in element(injections).text:
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)


    def is_title(self, expected_title, stop=False, skip=False):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that page title is '" + expected_title + "'.")
            observed_title = self._driver.title
            self.logger.log("EXPECTED: " + expected_title)
            self.logger.log("OBSERVED: " + observed_title)
            if observed_title == expected_title:
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
            else:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_title_contains(self, expected_title, stop=False, skip=False):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that page title contains '" + expected_title + "'.")
            observed_title = self._driver.title
            self.logger.log("EXPECTED: " + expected_title)
            self.logger.log("OBSERVED: " + observed_title)
            if expected_title in observed_title:
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
            else:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_page_url(self, expected_url, stop=False, skip=False):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that page URL is '" + expected_url + "'.")
            observed_url = self._driver.current_url
            self.logger.log("EXPECTED: " + expected_url)
            self.logger.log("OBSERVED: " + observed_url)
            if observed_url == expected_url:
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
            else:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_page_url_contains(self, expected_url, stop=False, skip=False):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that page URL contains '" + expected_url + "'.")
            observed_url = self._driver.current_url
            self.logger.log("EXPECTED: " + expected_url)
            self.logger.log("OBSERVED: " + observed_url)
            if expected_url in observed_url:
                self.logger.log("RESULT: PASS")
                self.passed_amount += 1
            else:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_attribute(self, element, attribute_name, attribute_value, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' contains attribute '" + attribute_name + "' with value '" + attribute_value + "'"
            self.logger.log(message)
            try:
                if element(injections).get_attribute(attribute_name) == attribute_value:
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_attribute_contains(self, element, attribute_name, attribute_value, stop=False, skip=False, injections=[]):
        self.logger.log(self.test_delimeter * 80, with_time=False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            message = "Verify that element with locator_type = '" + getattr(element, "locator_type", "UNKNOWN") + "' and locator = '" + getattr(element, "locator", "UNKNOWN") + "' contains in attribute '" + attribute_name + "' the value '" + attribute_value + "'"
            self.logger.log(message)
            try:
                if attribute_value in element(injections).get_attribute(attribute_name):
                    self.logger.log("RESULT: PASS")
                    self.passed_amount += 1
                else:
                    self.logger.log("RESULT: FAIL")
                    self.failed_amount += 1
            except:
                self.logger.log("RESULT: FAIL")
                self.failed_amount += 1
                if stop:
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time=False)

    def is_enabled(self, element, stop=False, skip=False, injections=[]):
        pass

    def is_disabled(self, element, stop=False, skip=False, injections=[]):
        pass

    def is_checked(self, element, stop=False, skip=False, injections=[]):
        pass

    def is_unchecked(self, element, stop=False, skip=False, injections=[]):
        pass








# ############ EXAMPLE ############################################
#     def isTrue(self, value, stop = False, skip = False):
#         self.logger.log(self.test_delimeter * 80, with_time = False)
#         if skip:
#             self.logger.log("SKIPPED")
#             self.skipped_amount += 1
#         else:
#             self.logger.log("Verify that " + str(value) + " is True.")
#             self.logger.log("EXPECTED: " + "True")
#             self.logger.log("OBSERVED: " + str(value))
#             if(value):
#                 self.logger.log("PASS")
#                 self.passed_amount += 1
#             else:
#                 self.logger.log("FAIL")
#                 self.failed_amount += 1
#             if(stop):
#                     raise AssertionError
#         self.logger.log(self.test_delimeter * 80, with_time = False)



## + verifyTitle
## + verifyProperty
## + verifyTextInjected
## + verifyText
##verifyTextFromActual
##verifyNotTextFromActual
##verifyLanguageOptionsList
##verifySelectedCountryNameById
## + verifyTextContains
## + verifyTextContainsInjected
##verifyLocation
##verifyLocationInjected
##verifySize
## + verifyURL
## + verifyPropertyInjected
## + verifyPropertyContains
##verifyTagName
##verifyIfNotTagNameInjected
##verifySelectionList
##verifySelectionList
##verifyOptionsNumber
##verifySelectedOption
##verifyElementState
##verifyElementEnabledState
##verifyIfDisplayed
##verifyIfDisplayedInjected
##verifyIfNotDisplayed
##verifyIfTextRed
##verifyIfNotPresentInjection
##verifyOptionsAmount
##verifyIfPresentInjection
##verifyIfFieldIsRequired
##verifyIfTextBolded
##verifyParagraphText
##verifyPosition
##verifyIfSectionExpanded
##verifyIfSectionCollapsed
##verifyElementDisabledState
##verifyCssStyleValue
##+verifyPageURL
## + verifyValue
##verifyCharsAmount
##verifyInnerText
##verifySortOrder
##verifyDate




