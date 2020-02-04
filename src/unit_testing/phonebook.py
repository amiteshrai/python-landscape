""" The PhoneBook Module """


class PhoneBook:
    """ The PhoneBook Class """

    def __init__(self):
        self.numbers = {}

    def lookup(self, name):
        """ Lookup for the given name """

        if not self.numbers[name]:
            raise KeyError("Entry for {} does not exist".format(name))

        return self.numbers[name]

    def lookup_by_name(self, name):
        """ Lookup number by name """

        return self.numbers[name]

    def add(self, name, number):
        """ Add an entry into numbers dictionary """

        self.numbers[name] = number

    def is_consistent(self):
        """ Check if the phonebook is consistent """
