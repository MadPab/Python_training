from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
        self.firstname = None
        self.lastname = None
        self.homephone = None
        self.mobilephone = None
        self.workphone = None
        self.secondaryphone = None
        self.id = None

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
        