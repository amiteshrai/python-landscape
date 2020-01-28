""" Logger Module """

import logging
import logging.config

# Configure logging
logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)


def get_logger(name):
    """
    Return a logger for the given module name

    Arguments:
        name {string} -- The name of the module

    Returns:
        [logging.logger] -- The logger instance
    """

    if not name:
        name = __name__

    return logging.getLogger(name)
