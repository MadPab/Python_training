from model.group2 import Group


def test_modify_contact_firstname(app):
    if app.group.count() == 0:
        app.group.create(Group(firstname="test"))
    app.group2.modify_first_contact(Group(firstname="New firstname"))

def test_modify_contact_lastname(app):
    if app.group.count() == 0:
        app.group.create(Group(latname="test"))
    app.group2.modify_first_contact(Group(latname="New lastname"))

def test_modify_contact_title(app):
    if app.group.count() == 0:
        app.group.create(Group(title="test"))
    app.group2.modify_first_contact(Group(title="New title"))

def test_modify_contact_company(app):
    if app.group.count() == 0:
        app.group.create(Group(company="test"))
    app.group2.modify_first_contact(Group(company="New lcompany"))

def test_modify_contact_address(app):
    if app.group.count() == 0:
        app.group.create(Group(address="test"))
    app.group2.modify_first_contact(Group(address="New address"))

def test_modify_contact_home(app):
    if app.group.count() == 0:
        app.group.create(Group(latname="test"))
    app.group2.modify_first_contact(Group(latname="New home"))

def test_modify_contact_mobile(app):
    if app.group.count() == 0:
        app.group.create(Group(mobile="test"))
    app.group2.modify_first_contact(Group(mobile="New mobile"))
