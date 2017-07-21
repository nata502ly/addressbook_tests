def test_group_create(app, init_login, group, db):
    old_group_list = db.get_group_list()
    app.open_group_page()
    app.group.create(group)
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()
    # Verifying group created in DB:
    new_group_list = db.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list) == sorted(new_group_list)
    # old_group_list.sort()
    # new_group_list.sort()
    # assert old_group_list == new_group_list
