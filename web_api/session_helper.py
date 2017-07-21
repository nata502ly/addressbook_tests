from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def is_logged(self):
        return self.app.is_element_present(By.NAME, 'logout')

    def login(self, username, password):
        wd = self.app.wd
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
        self.app.wd.find_element_by_css_selector("#top > form > a").click()
