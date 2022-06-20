import random
import string
from Remember_all.model.cont import Contact


constant = [
    
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(prefix, maxlen):
    symbols = string.digits + string.punctuation + " " * 1
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# [Contact(firstname="", middlename="", nickname="", title="", company="")] +

testdata = [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 5)
            , homephone=random_digits("+7383", 7), mobilephone=random_digits("8960", 7),
            workphone=random_digits("+7923", 7), fax=random_digits("fax", 5), email=random_string("email", 5),
            email2=random_string("email2", 5), email3=random_string("email3", 5), homepage=random_string("homepage", 5),
            address2=random_string("address2", 5), secondaryphone=random_digits("second", 5),
            notes=random_string("notes", 5)) for i in range(1)]

