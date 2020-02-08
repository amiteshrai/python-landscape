""" Test Employee Module """

import unittest
from unittest.mock import patch

from src.unit_testing.employee import Employee
from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


class TestEmployee(unittest.TestCase):
    """ Test Employee """

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def setUp(self):
        LOGGER.info("Setting Up Resources For Test Case...")
        super().setUp()
        self.employee1 = Employee("Amitesh", "Rai", 500000)
        self.employee2 = Employee("Amitesh", "Kumar", 500000)

    def tearDown(self):
        super().tearDown()
        self.addCleanup(self.cleanUp)

    def cleanUp(self) -> None:
        """ Clean up references to objects   """
        LOGGER.info("Cleaning Up Resources After Test Case...")

        self.employee1 = None
        self.employee2 = None

    def test_email(self) -> None:
        """ Test Employee Email """

        LOGGER.info("Testing Employee Email...")

        self.assertEqual(self.employee1.email, "Amitesh.Rai@example.com")
        self.assertEqual(self.employee2.email, "Amitesh.Kumar@example.com")

        self.employee2.last = "Rai"
        self.assertEqual(self.employee2.email, "Amitesh.Rai@example.com")

    def test_fullname(self) -> None:
        """ Test Employee Fullname """

        LOGGER.info("Testing Employee Fullname...")

        self.assertEqual(self.employee1.fullname, "Amitesh Rai")
        self.assertEqual(self.employee2.fullname, "Amitesh Kumar")

        self.employee2.last = "Rai"
        self.assertEqual(self.employee2.fullname, "Amitesh Kumar")

    def test_get_schedule(self) -> None:
        """ Test Employee Monthly Schedule """

        LOGGER.info("Testing Employee Schedule...")

        # Create a mock patch
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            # Test employee schedule using the mocked data created above
            schedule = self.employee1.get_schedule("February")
            mocked_get.assert_called_with(
                f"http://mycompany.com/{self.employee1.fullname}/February"
            )
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.employee2.get_schedule("March")
            mocked_get.assert_called_with(
                f"http://mycompany.com/{self.employee2.fullname}/March"
            )
            self.assertEqual(schedule, "Bad Response")


if __name__ == "__main__":
    # Run test cases
    unittest.main()
