import unittest
import cnjokes
import json    #def test_cnJokes(self):
    #    self.assertEqual("Chuck Norris knows the value of NULL, and he can sort by it too.", cnjokes.cnJokes("chuck norris"))


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.jokes = json.loads(open('fixtures/jokes.json', 'r').read())


    def test_cnJokes(self):
        self.assertEqual("Chuck Norris knows the value of NULL, and he can sort by it too.", cnjokes.getJoke(self.jokes))



if __name__ == '__main__':
    unittest.main()