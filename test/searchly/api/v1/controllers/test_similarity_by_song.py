import requests
import unittest

from src.searchly import API_SONG_SIMILARITY_LIMIT


class APISimilarityBySongTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8088/api/v1/similarity/by_song'
        self.song_id = 1
        self.song_id_not_found = -1
        self.status_code = 200

    def test_status_code(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, self.status_code)

    def test_missing_parameter(self):
        response = requests.get(self.url).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], '`song_id` missed as a query parameter.')

    def test_song_not_found(self):
        query_parameters = dict(song_id=self.song_id_not_found)
        response = requests.get(self.url, params=query_parameters).json()
        self.assertIn('error', response)
        self.assertIn('message', response)
        self.assertEqual(response['error'], True)
        self.assertEqual(response['message'], 'Song not found.')

    def test_response(self):
        query_parameters = dict(song_id=self.song_id)
        response = requests.get(self.url, params=query_parameters).json()
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
