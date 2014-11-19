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

from datetime import datetime
from Logger import *

class Verify(object):

    def __init__(
            self,
            logger,
            is_enabled = True,
            test_delimeter = '',
            locale = "ru",
            is_console = False,
            global_continue = None
    ):

        #
        self.is_enabled = is_enabled

        self.global_continue = global_continue

        self.logger = logger

        self.passed_amount = 0
        self.failed_amount = 0
        self.skipped_amount = 0

        self.test_delimeter = test_delimeter


    def print_header(self):
        pass

    def print_footer(self):
        self.logger.log(self.test_delimeter * 80, with_time = False)
        self.logger.log("TEST COMPLETE:")
        self.logger.log("TESTS PASSED: " + str(self.passed_amount))
        self.logger.log("TESTS FAILED: " + str(self.failed_amount))
        self.logger.log("TESTS SKIPPED: " + str(self.skipped_amount))
        self.logger.log(self.test_delimeter * 80, with_time = False)

    def log_test_result(self, result, message):
        self.logger.log(self.test_delimeter * 80, with_time = False)
        self.logger.log("Description: " + message)
        self.logger.log(result)
        self.logger.log(self.test_delimeter * 80, with_time = False)


   # Value verification

    def isTrue(self, value, stop = False, skip = False):
        self.logger.log(self.test_delimeter * 80, with_time = False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that " + str(value) + " is True.")
            self.logger.log("EXPECTED: " + "True")
            self.logger.log("OBSERVED: " + str(value))
            if(value):
                self.logger.log("PASS")
                self.passed_amount += 1
            else:
                self.logger.log("FAIL")
                self.failed_amount += 1
            if(stop):
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time = False)


    def isFalse(self, value, stop = False, skip = False):
        self.logger.log(self.test_delimeter * 80, with_time = False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that " + str(value) + " is True.")
            self.logger.log("EXPECTED: " + "False")
            self.logger.log("OBSERVED: " + str(value))
            if( not value):
                self.logger.log("PASS")
                self.passed_amount += 1
            else:
                self.logger.log("FAIL")
                self.failed_amount += 1
            if(stop):
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time = False)



    def isEqual(self, expected, observed, stop = False, skip = False):
        self.logger.log(self.test_delimeter * 80, with_time = False)
        if skip:
            self.logger.log("SKIPPED")
            self.skipped_amount += 1
        else:
            self.logger.log("Verify that " + str(observed) + " equals to " + str(expected))
            self.logger.log("EXPECTED: " + str(expected))
            self.logger.log("OBSERVED: " + str(observed))
            if(expected == observed):
                self.logger.log("PASS")
                self.passed_amount += 1
            else:
                self.logger.log("FAIL")
                self.failed_amount += 1
            if(stop):
                    raise AssertionError
        self.logger.log(self.test_delimeter * 80, with_time = False)



#Simple testing of module
#TODO: Should be added file comparing of  generated file and sample
if __name__ == '__main__':

    script_name = "../Reports/testty_script"

    verify = Verify(script_name)
    verify.isTrue(12)
    verify.isTrue(False)

    verify.isEqual(23, 23)
    verify.isEqual(23, 7)

    verify.print_footer()
