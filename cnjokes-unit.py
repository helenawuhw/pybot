import unittest
import cnjokes
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.jokes = json.loads(open('fixtures/jokes.json', 'r').read())


    def test_cnJokes(self):
        self.assertEqual(None, cnjokes.cnJokes(''))

    def test_cnJokes(self):
        self.assertEqual("Chuck Norris knows the value of NULL, and he can sort by it too.", cnjokes.cnJokes("chuck norris"))







if __name__ == '__main__':
    unittest.main()