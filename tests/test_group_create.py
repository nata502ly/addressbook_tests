def test_group_create(app, init_login, group):
    app.open_group_page()
    app.group.create(group)
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()
    # TODO: Verify group created
