"""
    Python Interfaces Module
    ========================

    Interfaces play an important role in software engineering. As an application grows,
    updates and changes to the code base become more difficult to manage.

    More often than not, you wind up having classes that look very similar but are
    unrelated, which can lead to some confusion.
"""


from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

# 1. Informal Interface:

# An informal Python interface is a class that defines methods that can be overridden,
# but there’s no strict enforcement.


class DataParserInterface:
    """ Defines a data parser interface """

    def load_data(self, path: str, filename: str) -> str:
        """
        Description: Load in the file for extraction

        Arguments:
            path {str} -- base path to search the file in
            filename {str} -- filename to be loaded in memory

        Returns:
            str -- See the method implementing this interface
        """

    def extract_data(self, filepath: str) -> dict:
        """
        Description: Extract data from the given file

        Arguments:
            filepath {str} -- The complete path of the file to be extracted

        Returns:
            dict -- See the method implementing this interface
        """
