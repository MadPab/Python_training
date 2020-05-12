class GroupHelper:

    def __int__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_name("add").click()

    def create(self, firstname, lastname, title, company, address, home, mobile):
        wd = self.app.wd
        self.fill_contact_form(address, company, firstname, home, lastname, mobile, title)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_contact_form(self, group2):
        wd = self.app.wd
        self.change_fill_value("contact_firstname", group2.firstname)
        self.change_fill_value("contact_lastname", group2.lastname)
        self.change_fill_value("contact_title", group2.title)
        self.change_fill_value("contact_company", group2.company)
        self.change_fill_value("contact_address", group2.address)
        self.change_fill_value("contact_home", group2.home)
        self.change_fill_value("contact_mobile", group2.mobile)

    def change_fill_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_name("Edit").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("Update").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        