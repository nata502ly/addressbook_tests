from selenium import webdriver
import unittest


class test_group_create(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_test_group_create(self):
        wd = self.wd
        # Open main page
        wd.get("http://localhost/addressbook/index.php")
        # Login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # Open group page
        wd.find_element_by_css_selector("#nav > ul > li.admin > a").click()
        # Create
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("00000090000")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("00000")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("000000")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[11]").click()
        wd.find_element_by_name("submit").click()
        # TODO: Verify message
        # Return to group page
        wd.find_element_by_link_text("group page").click()
        # Logout
        wd.find_element_by_css_selector("#top > form > a").click()
        # TODO: Verify group created

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
