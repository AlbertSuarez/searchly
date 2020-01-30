from expiringdict import ExpiringDict

from src.searchly import CACHE_MAX_LENGTH, CACHE_MAX_AGE, CACHE_DICT_FORMAT


__cache = ExpiringDict(max_len=CACHE_MAX_LENGTH, max_age_seconds=CACHE_MAX_AGE)  # 5 minutes expiration


def get(method, key):
    """
    Get object from the cache given a method and key.
    :param method: Method.
    :param key: Key.
    :return: Cached object if found, None otherwise.
    """
    return __cache.get(CACHE_DICT_FORMAT.format(method, key))


def refresh(method, key, refreshed_element):
    """
    Refresh object in cache.
    :param method: Method.
    :param key: Key.
    :param refreshed_element: Object to refresh.
    :return: Object refreshed.
    """
    __cache[CACHE_DICT_FORMAT.format(method, key)] = refreshed_element
