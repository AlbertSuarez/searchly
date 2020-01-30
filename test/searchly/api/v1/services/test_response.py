import unittest

from src.searchly.api.v1.services import response


class ResponseTest(unittest.TestCase):

    def setUp(self):
        self.message = 'Error message'
        self.key = 'key'
        self.key_not_found = 'random'
        self.default_not_found = 'not found, bro'
        self.value = 'value'
        self.dict = {self.key: self.value}

    def test_get_found(self):
        value = response.get(self.key, self.dict)
        self.assertEqual(value, self.value)

    def test_get_not_found(self):
        value = response.get(self.key_not_found, self.dict, default=self.default_not_found)
        self.assertEqual(value, self.default_not_found)
