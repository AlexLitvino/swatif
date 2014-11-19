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

def main():
    pass

if __name__ == '__main__':
    main()


class BasePage(object):

    def __init__(self, driver):
        self._driver = driver


    def get_title(self):
        return _driver.title



    def scroll_page_down(self):
        pass

    def scroll_page_up(self):
        pass

    def navigateTo(self):
        pass


    def back(self):
        self._driver.back()

    def forward(self):
        self._driver.forward()

    def refresh(self):
        self._driver.refresh()

    def get_page_source():
        return self._driver.page_source();




