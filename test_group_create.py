from models.group import Group


def test_group_create(app, init_login):
    group = Group(name="00000090000", header="00000", footer="000000")
    app.open_group_page()
    app.create_group(group)
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()
    # TODO: Verify group created

