from model.group2 import Group


def test_modify_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.create(Group(firstname="as", lastname="asd", title="a", company="s", address="vbnvvn", home="cvv", mobile="543435")
    app.session2.logout()