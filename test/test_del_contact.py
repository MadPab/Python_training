from model.group2 import Group

def test_delete_first_contact(app):
    if app.group2.count() == 0:
        app.group2.create(Group(firstname="test"))
    app.group2.delete_first_contact()
