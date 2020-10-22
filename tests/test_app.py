import sqlite3
import unittest

from app import get_movies_by_actor, get_actor_bacon_degree, search_actors_by_name

class TestDatabaseLayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect("bacon.db")

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    def test_database_access_functions(self):
        cur = self.conn.cursor()

        actors = search_actors_by_name(cur, "Kevin Bacon")
        self.assertEqual(len(actors), 1)
        actor_id = actors[0]
        movies = get_movies_by_actor(cur, actor_id)
        self.assertEqual(len(movies), 63)
        degree = get_actor_bacon_degree(cur, actor_id)
        self.assertEqual(degree, 0)

