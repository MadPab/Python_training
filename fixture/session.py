from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def ensure_login(self, username, password):
        if self.is_loggined() > 0:
            if self.check_loggined_name() != username:
                self.logout()
            else:
                return
        self.login(username, password)

    def check_loggined_name(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@id='top']/form/b").text[1:-1]

    def is_loggined(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout"))

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()
