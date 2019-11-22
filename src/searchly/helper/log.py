import logging
import sys


# Setup main loggers
__logger_stdout = logging.getLogger('searchly')

# Setup formatter
__formatter = logging.Formatter('{%(name)s} - <%(asctime)s> - [%(levelname)-7s] - %(message)s')

# Setup stdout stream handler
__handler_stdout = logging.StreamHandler(sys.stdout)
__handler_stdout.setFormatter(__formatter)
__logger_stdout.addHandler(__handler_stdout)
__logger_stdout.setLevel(logging.INFO)


def debug(msg):
    """
    Optimized debugging log call which wraps with debug check to prevent unnecessary string creation.
    :param msg: Message to debug.
    :return: Message debugged.
    """
    if __logger_stdout.isEnabledFor(logging.DEBUG):
        __logger_stdout.debug(msg)


def info(msg):
    """
    Log [INFO] level log messages.
    :param msg: Message to info.
    :return: Message informed.
    """
    __logger_stdout.info(msg)


def warn(msg):
    """
    Log [WARNING] level log messages.
    :param msg: Message to warn.
    :return: Message warned.
    """
    __logger_stdout.warning(msg)


def error(msg):
    """
    Log [ERROR] level log messages.
    :param msg: Message to error.
    :return: Message notified as error.
    """
    __logger_stdout.error(msg)


def exception(msg):
    """
    Log [ERROR] level log messages.
    :param msg: Message to except.
    :return: Message excepted.
    """
    __logger_stdout.exception(msg)
