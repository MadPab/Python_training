from sys import maxsize

class Group:

    def __int__(self, firstname=None, lastname=None, title=None, company=None, address=None, home=None, mobile=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.title, self.company, self.address, self.home, self.mobile)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

