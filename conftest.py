import json
import os.path

import pytest

from data.groups_data import groups_list
from models.group import Group
from web_api.addressbook_api import AddressBook
from db_api.addressbook_db import AddressbookDB


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json")


@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_name) as f:
        return json.load(f)


@pytest.fixture()
def app(selenium, config):
    app = AddressBook(selenium, base_url=config["web"]["base_url"])
    app.open_main_page()
    yield app
    app.destroy()


@pytest.fixture(scope="session")
def db(config):
    dbfixture = AddressbookDB(**config["db"])
    yield dbfixture
    dbfixture.close()


@pytest.fixture()
def init_login(app, config):
    if not app.session.is_logged():
        app.session.login(username=config["web"]["username"], password=config["web"]["password"])
    yield
    app.session.logout()


@pytest.fixture()
def init_group(app, init_login):
    if not app.group.is_present():
        app.group.create(Group(name="Test"))


@pytest.fixture(params=groups_list, ids=[str(g) for g in groups_list])
def group(request):
    return request.param
