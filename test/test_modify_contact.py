from model.group2 import Group


def test_modify_contact_firstname(app):
    app.group2.modify_first_contact(Group(firstname="New firstname"))

def test_modify_contact_lastname(app):
    app.group2.modify_first_contact(Group(latname="New lastname"))

def test_modify_contact_title(app):
    app.group2.modify_first_contact(Group(title="New title"))

def test_modify_contact_company(app):
    app.group2.modify_first_contact(Group(company="New lcompany"))

def test_modify_contact_address(app):
    app.group2.modify_first_contact(Group(address="New address"))

def test_modify_contact_home(app):
    app.group2.modify_first_contact(Group(latname="New home"))

def test_modify_contact_mobile(app):
    app.group2.modify_first_contact(Group(mobile="New mobile"))
