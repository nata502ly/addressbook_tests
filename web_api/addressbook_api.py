from selenium import webdriver
from web_api.group_helper import GroupHelper
from web_api.session_helper import SessionHelper


class AddressBook:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(1)
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_main_page(self):
        self.wd.get(self.base_url)

    def is_element_present(self, by, value):
        return not len(self.wd.find_elements(by, value)) == 0

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_css_selector("#nav > ul > li.admin > a").click()

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def message(self):
        return self.wd.find_element_by_css_selector('#content > div').text

    def destroy(self):
        self.wd.quit()
