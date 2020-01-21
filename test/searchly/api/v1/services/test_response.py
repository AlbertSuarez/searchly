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

    def test_make_error(self):
        json_response, status_code = response.make(error=True, message=self.message)
        self.assertIs(type(json_response), dict)
        self.assertIs(type(status_code), int)
        self.assertIn('error', json_response)
        self.assertIn('message', json_response)
        self.assertEqual(json_response['error'], True)
        self.assertEqual(json_response['message'], self.message)
        self.assertEqual(status_code, 200)

    def test_make_success(self):
        json_response, status_code = response.make(error=False, response=self.dict)
        self.assertIs(type(json_response), dict)
        self.assertIs(type(status_code), int)
        self.assertIn('error', json_response)
        self.assertIn('response', json_response)
        self.assertIn(self.key, json_response['response'])
        self.assertEqual(json_response['error'], False)
        self.assertEqual(json_response['response'][self.key], self.value)
        self.assertEqual(status_code, 200)

    def test_get_found(self):
        value = response.get(self.key, self.dict)
        self.assertEqual(value, self.value)

    def test_get_not_found(self):
        value = response.get(self.key_not_found, self.dict, default=self.default_not_found)
        self.assertEqual(value, self.default_not_found)
