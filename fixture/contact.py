import re
from selenium.webdriver.common.by import By
from Remember_all.model.cont import Contact


class ContactHelper:
    contact_cache = None

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element(By.LINK_TEXT, "home").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.CSS_SELECTOR, "input[name='selected[]'")[index].click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        wd.find_element(By.XPATH, "//input[@name='submit'][2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_name("firstname", contact.firstname)
        self.change_field_name("middlename", contact.middlename)
        self.change_field_name("lastname", contact.lastname)
        self.change_field_name("nickname", contact.nickname)
        self.change_field_name("title", contact.title)
        self.change_field_name("company", contact.company)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.homephone)
        self.change_field_name("mobile", contact.mobilephone)
        self.change_field_name("work", contact.workphone)
        self.change_field_name("fax", contact.fax)
        self.change_field_name("email", contact.email)
        self.change_field_name("email2", contact.email2)
        self.change_field_name("email3", contact.email3)
        self.change_field_name("homepage", contact.homepage)
        self.change_field_name("address2", contact.address2)
        self.change_field_name("phone2", contact.secondaryphone)
        self.change_field_name("notes", contact.notes)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]'))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, ' tr[name="entry"]'):
                cells = element.find_elements(By.TAG_NAME, 'td')
                lastname = element.find_element(By.XPATH, "td[2]").text
                firstname = element.find_element(By.XPATH, "td[3]").text
                id_contact = wd.find_element(By.CSS_SELECTOR, 'td input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id_contact,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def update_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.CSS_SELECTOR, 'img[title="Edit"]').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete"]').click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.XPATH, '//img[@title="Edit"]')[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.CSS_SELECTOR, ' tr[name="entry"]')[index]
        cell = row.find_elements(By.TAG_NAME, 'td')[6]
        cell.find_element(By.TAG_NAME, 'a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = wd.find_element(By.NAME, 'lastname').get_attribute('value')
        id = wd.find_element(By.NAME, 'id').get_attribute('value')
        homephone = wd.find_element(By.NAME, 'home').get_attribute('value')
        workphone = wd.find_element(By.NAME, 'work').get_attribute('value')
        mobilephone = wd.find_element(By.NAME, 'mobile').get_attribute('value')
        secondaryphone = wd.find_element(By.NAME, 'phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, 'content').text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
