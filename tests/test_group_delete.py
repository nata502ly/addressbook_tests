import random


def test_group_create(app, init_login, init_group):
    index = random.randrange(app.group_count())
    app.open_group_page()
    app.delete_group(index)
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
    # TODO: Verify group deleted
