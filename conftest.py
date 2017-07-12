import pytest
from addressbook_api import AddressBook

@pytest.fixture()
def app():
    a = AddressBook()
    yield a
    a.destroy()
