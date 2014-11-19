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

import sys

def adding_leading_zero(number):
    """
    Adding leading zero for numbers less than 10
    """
    return str(number) if number > 9 else '0' + str(number)


##class Logger(object):
##    def __init__(self, filename="Default.log"):
##        self.terminal = sys.stdout
##        self.log = open(filename, "a")
##
##    def write(self, message):
##        self.terminal.write(message)
##        self.log.write(message)









class Logger(object):
    """
    Class to log data from script
    """

    def __init__(self, output_file, with_date = True, locale = "ru"):
        self.console = sys.stdout
        self.output_file = output_file

        if with_date:
            current_datetime = datetime.now()
            day = adding_leading_zero(current_datetime.day)
            month = adding_leading_zero(current_datetime.month)
            year = adding_leading_zero(current_datetime.year)
            hour = adding_leading_zero(current_datetime.hour)
            minute = adding_leading_zero(current_datetime.minute)
            second = adding_leading_zero(current_datetime.second)
            if locale == "ru":
                s = day + month + year + '_' + hour + minute + second
            elif locale == "en":
                s = month + day + year + '_' + hour + minute + second
            self.output_file = output_file + '_' + s + ".log"
        else:
            self.output_file = output_file + ".log"


    def log(self, message, with_time = True):
        with open(self.output_file, 'a') as f:
            if with_time:
                current_time = datetime.now().time()
                hour = str(current_time.hour)
                minute = str(current_time.minute)
                second = str(current_time.second)
                millisecond = str(current_time.microsecond)#transfer to milliseconds
                f.write('[' + hour + ':' + minute + ':' + second + '.' + millisecond +']' + ' ')
            f.write(message + '\n')
            self.console.write(message + '\n')


    def log_test(self, message, with_time = True):
        if(self.output_file == None):
            f = sys.stdout
        else:
            f = open(self.output_file, 'a')


        if with_time:
            current_time = datetime.now().time()
            #print(str(type(current_time)))
            hour = str(current_time.hour)
            minute = str(current_time.minute)
            second = str(current_time.second)
            millisecond = str(current_time.microsecond)#transfer to milliseconds
            f.write('[' + hour + ':' + minute + ':' + second + '.' + millisecond +']' + ' ')
        f.write(message)
        f.write('\n')








def main():
    pass

if __name__ == '__main__':
    main()
    logger1 = Logger("simple_logger.txt")
    logger = Logger(None)
    logger.log_test("1")
    logger.log_test("10")

