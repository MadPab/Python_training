# -*- coding: utf-8 -*-
import pytest
from fixture.application2 import Application2


@pytest.fixture()
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(firstname="as", lastname="asd", title="a", company="s", address="vbnvvn", home="cvv", mobile="543435")
        app.logout()

def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(firstname="", lastname="", title="", company="", address="", home="", mobile="")
        app.logout()

