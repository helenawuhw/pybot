import unittest
import metro
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      self.orderedMetroData = json.loads(open('fixtures/ordered.json', 'r').read())
      self.unorderedMetroData = json.loads(open('fixtures/unordered.json', 'r').read())
      self.test2MetroData = json.loads(open('fixtures/test2.json', 'r').read())


    def test_ordered_timeForNextTrainToV(self):
        self.assertEqual("2", metro.timeForNextTrainToV(self.orderedMetroData))

    def test_ordered_timeForNextTrainToNC(self):
        self.assertEqual("1", metro.timeForNextTrainToNC(self.orderedMetroData))

    def test_unordered_timeForNextTrainToV(self):
        self.assertEqual("2", metro.timeForNextTrainToV(self.unorderedMetroData))

    def test_unordered_timeForNextTrainToNC(self):
        self.assertEqual("1", metro.timeForNextTrainToNC(self.unorderedMetroData))
  
    def test_unordered_timeForNextTrainToL(self):
      self.assertEqual(None, metro.timeForNextTrainToL(self.unorderedMetroData))
      
    def test_test2_timeForNextTrainToV(self):
      self.assertEqual("2", metro.timeForNextTrainToV(self.test2MetroData))
      
    def test_test2_timeForNextTrainToNC(self):
      self.assertEqual("1", metro.timeForNextTrainToNC(self.test2MetroData))
      
    def test_test2_timeForNextTrainToL(self):
      self.assertEqual("11", metro.timeForNextTrainToL(self.test2MetroData))
      
      
if __name__ == '__main__':
    unittest.main()
