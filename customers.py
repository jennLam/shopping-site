"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email;
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""
        return "<Customer: %s, %s, %s, %s>" % (
                self.first_name, self.last_name, self.email, self.password)

customer_dict = {}

def read_file(file_name):
    text_file = open(file_name)
    for line in text_file:
        line = line.rstrip()
        words = line.split("|")
        customer_dict[words[2]] = Customer(words[0], words[1], words[2], words[3])
        # print words[3], words[2], words[1], words[0]
        # print customer_dict[words[3]]
        return customer_dict

def get_by_email(email):

    return customer_dict.get(email)


read_file("customers.txt")




