# -*- coding: utf-8 -*-
from random import randrange
from Remember_all.model.cont import Contact


def test_update_some_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    cont = Contact(firstname="Ivan", lastname="Ivanov")
    cont.id = old_contacts[index].id
    app.contact.update_contact_by_index(index, cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # old_contacts[index] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
