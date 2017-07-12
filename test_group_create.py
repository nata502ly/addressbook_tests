from addressbook_api import AddressBook
from models.group import Group
import unittest



class test_group_create(unittest.TestCase):
    def setUp(self):
        self.app = AddressBook()

    def test_test_group_create(self):
        group = Group(name="00000090000", header="00000", footer="000000")
        self.app.open_main_page()
        self.app.login(username="admin", password="secret")
        self.app.open_group_page()
        self.app.create_group(group)
        # TODO: Verify message
        self.app.return_to_group_page()
        self.app.logout()
        # TODO: Verify group created

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
