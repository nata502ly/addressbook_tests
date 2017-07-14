from selenium import webdriver
from selenium.webdriver.common.by import By


class AddressBook:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)

    def open_main_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, by, value):
        return not len(self.wd.find_elements(by, value)) == 0

    def is_logged(self):
        return self.is_element_present(By.NAME, 'logout')

    def is_groups_present(self):
        self.open_group_page()
        return self.is_element_present(By.NAME, "selected[]")

    def group_count(self):
        self.open_group_page()
        return len(self.wd.find_elements_by_name("selected[]"))

    def login(self, username, password):
        wd = self.wd
        # Fill form login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # Submit login
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        # Logout
        self.wd.find_element_by_css_selector("#top > form > a").click()

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_css_selector("#nav > ul > li.admin > a").click()

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        # Create
        wd.find_element_by_name("new").click()
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").click()
        wd.find_element_by_name("submit").click()

    def delete_group(self, index):
        wd = self.wd
        checkboxes = wd.find_elements_by_name('selected[]')
        if not checkboxes[index].is_selected():
            checkboxes[index].click()
        button = wd.find_element_by_name("delete")
        button.click()


    def message(self):
        return self.wd.find_element_by_css_selector('#content > div').text

    def destroy(self):
        self.wd.quit()
