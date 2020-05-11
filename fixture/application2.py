from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session2 import SessionHelper
from fixture.group2 import GroupHelper


class Application2:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session2 = SessionHelper(self)
        self.group2 = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")


    def destroy(self):
        self.wd.quit()
