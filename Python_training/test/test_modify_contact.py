from Python_training.model.group2 import Group
from random import randrange

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Group(firstname="Test", lastname="Testovich"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact=Group(firstname="Petr", lastname="Petrov")
    contact.id=old_contacts[index].id
    #contact.firstname=old_contacts[0].firstname
    app.contact.modify_contact_by_index(index=index, new_contact_data=contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)

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
