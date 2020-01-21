import requests
import unittest

from src.searchly import *


class APISongSearchTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8088/api/v1/song/search'
        self.query = 'cyrus'
        self.query_too_short = ' hi '
        self.status_code = 200

    def test_status_code(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, self.status_code)

    def test_missing_parameter(self):
        response = requests.get(self.url).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], '`query` missed as a query parameter.')

    def test_query_too_short(self):
        query_parameters = dict(query=self.query_too_short)
        response = requests.get(self.url, params=query_parameters).json()
        self.assertIn('error', response)
        self.assertIn('response', response)
        self.assertIn('results', response['response'])
        self.assertEqual(response['error'], False)
        self.assertEqual(len(response['response']['results']), 0)

    def test_response(self):
        query_parameters = dict(query=self.query)
        response = requests.get(self.url, params=query_parameters).json()
        self.assertIn('error', response)
        self.assertIn('response', response)
        self.assertIn('results', response['response'])
        self.assertEqual(response['error'], False)
        self.assertIs(type(response['response']['results']), list)
        self.assertGreater(len(response['response']['results']), 0)
        self.assertLessEqual(len(response['response']['results']), API_SONG_SEARCH_LIMIT)
        for result in response['response']['results']:
            self.assertIn('id', result)
            self.assertIn('name', result)
