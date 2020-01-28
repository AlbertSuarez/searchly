import requests
import unittest

from src.searchly import API_SONG_SIMILARITY_LIMIT


class APISimilarityByContentTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8088/api/v1/similarity/by_content'
        self.content = 'I love you.'
        self.content_wrong = 'And'
        self.status_code = 200

    def test_status_code(self):
        response = requests.post(self.url)
        self.assertEqual(response.status_code, self.status_code)

    def test_missing_parameter(self):
        response = requests.post(self.url).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], '`content` missed as a request json parameter.')

    def test_wrong_content(self):
        request_body = dict(content=self.content_wrong)
        response = requests.post(self.url, json=request_body).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], 'Could not be possible to extract features from it.')

    def test_response(self):
        request_body = dict(content=self.content)
        response = requests.post(self.url, json=request_body).json()
        self.assertIn('error', response)
        self.assertIn('response', response)
        self.assertIn('similarity_list', response['response'])
        self.assertEqual(response['error'], False)
        self.assertIs(type(response['response']['similarity_list']), list)
        self.assertGreater(len(response['response']['similarity_list']), 0)
        self.assertLessEqual(len(response['response']['similarity_list']), API_SONG_SIMILARITY_LIMIT)
        for similarity in response['response']['similarity_list']:
            self.assertIn('id', similarity)
            self.assertIn('artist_name', similarity)
            self.assertIn('song_name', similarity)
            self.assertIn('lyrics', similarity)
            self.assertIn('artist_url', similarity)
            self.assertIn('song_url', similarity)
            self.assertIn('index_id', similarity)
