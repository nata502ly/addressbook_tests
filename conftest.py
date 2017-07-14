import pytest
from addressbook_api import AddressBook


@pytest.fixture(scope="session")
def app():
    app = AddressBook()
    app.open_main_page()
    yield app
    app.destroy()


@pytest.fixture()
def init_login(app):
    if not app.is_logged():
        app.login(username="admin", password="secret")
    yield
    app.logout()
