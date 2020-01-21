import requests
import unittest


class APIErrorNotFoundTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8088/not_found'
        self.error_code = 404

    def test_error_code(self):
        response = requests.post(self.url)
        self.assertEqual(response.status_code, self.error_code)

    def test_response(self):
        response = requests.post(self.url).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], 'Not found.')

