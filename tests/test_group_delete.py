import random


def test_group_delete(app, init_login, init_group, db):
    old_group_list = db.get_group_list()
    index = random.randrange(app.group.count())
    app.open_group_page()
    app.group.delete(index)
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
    new_group_list = db.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list.pop(index)
    assert old_group_list == new_group_list
