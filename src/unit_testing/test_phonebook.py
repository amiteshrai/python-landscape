""" The PhoneBook Unit Test Module """

import unittest

from src.unit_testing.phonebook import PhoneBook
from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


class PhoneBookTest(unittest.TestCase):
    """ The PhoneBook Test Class """

    def setUp(self) -> None:
        """ Overriding setUp from TestCase class """

        LOGGER.info("Setting Up Resources...")
        self.phonebook = PhoneBook()

    def tearDown(self):
        """ Clean/Release All Resources For Test Cases """

        LOGGER.info("Releasing All Resources...")
        self.phonebook = None

    def test_lookup_by_name(self):
        """ Test lookup_by_name """

        LOGGER.info("Testing lookup_by_name..")
        self.phonebook.add("Amitesh", 292291911)
        number = self.phonebook.lookup_by_name("Amitesh")
        self.assertEqual(292291911, number, "Numbers not matching!")

    def test_missing_name(self):
        """ Test for missing names """

        LOGGER.info("Testing for missing names...")
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    @unittest.skip("WIP")
    def test_empty_phonebooks_consistency(self):
        """ Test if the PhoneBook is consistent """

        LOGGER.de("Testing phonebook's consitency...")
        self.assertTrue(self.phonebook.is_consistent())
