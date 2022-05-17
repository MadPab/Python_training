import pytest
from fixture.application2 import Application2

fixture = None

@pytest.fixture(scope = "session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application2()
        fixture.session2.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application2()
            fixture.session2.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session2.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture