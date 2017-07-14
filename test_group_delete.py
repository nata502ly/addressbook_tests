def test_group_create(app):
    app.open_main_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.delete_first_group()
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
    # TODO: Verify group deleted
    app.logout()
