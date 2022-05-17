# -*- coding: utf-8 -*-
from Python_training.model.group2 import Group


def test_add_contact(app):
        app.group2.create(Group(firstname="as", lastname="asd", title="a", company="s", address="vbnvvn", home="cvv", mobile="543435"))

def test_add_empty_contact(app):
        app.group2.create(Group(firstname="", lastname="", title="", company="", address="", home="", mobile=""))
