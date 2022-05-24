# -*- coding: utf-8 -*-
from Remember_all.model.cont import Contact
from Remember_all.fixture.app_contact import ApplicationContact
import pytest


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="abc", lastname="def"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="", lastname=""))
    app.logout()