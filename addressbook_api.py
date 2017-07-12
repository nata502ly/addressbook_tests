from selenium import webdriver


class AddressBook:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def logout(self):
        # Logout
        self.wd.find_element_by_css_selector("#top > form > a").click()

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        # Create
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").click()
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_css_selector("#nav > ul > li.admin > a").click()

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

    def open_main_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()