from selenium.webdriver.common.by import By
from Remember_all.model.group import Group


class GroupHelper:

    group_cache = None

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group/php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def update_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'span.group'):
                text = element.text
                id_ = element.find_element(By.NAME, 'selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id_))
        return list(self.group_cache)
