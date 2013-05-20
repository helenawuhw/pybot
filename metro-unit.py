import unittest
import metro
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      self.orderedMetroData = json.loads(open('fixtures/ordered.json', 'r').read())
      self.unorderedMetroData = json.loads(open('fixtures/unordered.json', 'r').read())

    def test_ordered_timeForNextWestTrain(self):
        self.assertEqual("2", metro.timeForNextWestTrain(self.orderedMetroData))

    def test_ordered_timeForNextEastTrain(self):
        self.assertEqual("1", metro.timeForNextEastTrain(self.orderedMetroData))

    def test_unordered_timeForNextWestTrain(self):
        self.assertEqual("2", metro.timeForNextWestTrain(self.unorderedMetroData))

    def test_unordered_timeForNextEastTrain(self):
        self.assertEqual("1", metro.timeForNextEastTrain(self.unorderedMetroData))

if __name__ == '__main__':
    unittest.main()


