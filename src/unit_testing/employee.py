""" Employee Module """

import requests


class Employee:
    """ An Employee Class """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self._increment = 1.2

    @property
    def email(self) -> str:
        """ Return employee email """

        return "{}.{}@example.com".format(self.first, self.last)

    @property
    def fullname(self) -> str:
        """ Return employee full name """

        return "{} {}".format(self.first, self.last)

    @property
    def increment(self) -> float:
        """ Get value of _increment property """

        return self._increment

    @increment.setter
    def increment(self, value) -> None:
        """ Set value of _increment property """

        self._increment = value

    def apply_raise(self) -> None:
        """ Apply increment in employee compensation """

        self.pay = int(self.pay * self._increment)

    def get_schedule(self, month) -> str:
        """ Get Employee Monthly Schedule """

        response = requests.get(f"http://mycompany.com/{self.fullname}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
