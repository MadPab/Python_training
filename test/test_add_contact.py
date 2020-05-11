# -*- coding: utf-8 -*-
import pytest
from model.group2 import Group
from fixture.application2 import Application2


@pytest.fixture()
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
        app.session2.login(username="admin", password="secret")
        app.create(firstname="as", lastname="asd", title="a", company="s", address="vbnvvn", home="cvv", mobile="543435")
        app.session2.logout()

def test_add_empty_contact(app):
        app.session2.login(username="admin", password="secret")
        app.create(firstname="", lastname="", title="", company="", address="", home="", mobile="")
        app.session2.logout()

