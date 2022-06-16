# -*- coding: utf-8 -*-
from Remember_all.model.cont import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="Ivan", lastname="Ivanov", workphone="8-912-345-67-89", homephone="8 900 000 00 00",
                   secondaryphone="+7 912-345-00 00", mobilephone="+79999999999")
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="", lastname="", workphone="", homephone="", secondaryphone="", mobilephone="")
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
