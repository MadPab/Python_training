from model.group2 import Group


def test_modify_contact_firstname(app):
    app.session2.login(username="admin", password="secret")
    app.group2.modify_first_contact(Group(firstname="New firstname"))
    app.session2.logout()

def test_modify_contact_lastname(app):
    app.session2.login(username="admin", password="secret")
    app.group2.modify_first_contact(Group(latname="New lastname"))
    app.session2.logout()