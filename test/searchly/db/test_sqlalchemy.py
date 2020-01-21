import unittest

from src.searchly.db import sqlalchemy


class ResponseTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_import(self):
        self.assertIsNotNone(sqlalchemy.engine)
        self.assertIsNotNone(sqlalchemy.meta)
        self.assertIsNotNone(sqlalchemy.db_session)
        self.assertIsNotNone(sqlalchemy.Base)
