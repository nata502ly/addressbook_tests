def test_modify_group(app, init_login, init_group):
    data_for_changing = Group()
    app.open_group_page()
    app.modify_group(index, data_for_changing)
    assert "........" in app.message()
    app.return_to_group_page()
