# -*- coding: utf-8 -*-
import pytest
from Remember_all.model.cont import Contact
from Remember_all.data.add_contact import testdata


@pytest.mark.parametrize("cont", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, cont):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
