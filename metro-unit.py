import unittest
import metro
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      self.orderedMetroData = json.loads(open('fixtures/ordered.json', 'r').read())
      self.unorderedMetroData = json.loads(open('fixtures/unordered.json', 'r').read())
      self.test2MetroData = json.loads(open('fixtures/test2.json', 'r').read())


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

    def test_shouldRespond_empty_string(self):
      self.assertEquals(False, metro.shouldRespond(''))

    def test_shouldRespond_obot(self):
      self.assertEquals(False, metro.shouldRespond('obot image me dog laughing'))

    def test_shouldRespond_not_relevant(self):
      self.assertEquals(False, metro.shouldRespond('here is the ticket in jira'))

    def test_shouldRespond_false(self):
      self.assertEquals(False, metro.shouldRespond('my favorite command is "obot show me metro"'))      

    def test_shouldRespond_true(self):
      self.assertTrue(metro.shouldRespond('obot show me metro'))      

    def test_shouldRespond_extra_space_at_end(self):
      self.assertTrue(metro.shouldRespond('obot show me metro       '))      

    def test_shouldRespond_extra_space_between_words(self):
      self.assertTrue(metro.shouldRespond('obot    show me     metro'))

    def test_shouldRespond_extra_space_at_beginning(self):
      self.assertTrue(metro.shouldRespond('      obot show me metro'))
    
    def test_shouldRespond_extra_space_at_beginning(self):
      self.assertEquals(False, metro.shouldRespond('      obot    / show me metro'))

    def test_formatTime(self):
      self.assertEquals('The next train to Vienna is in 5 minutes', metro.formatTime('Vienna', '5'))

    def test_formatTime_no_train(self):
      self.assertEquals('There is no schedule train going to Largo', metro.formatTime('Largo', None))
      
if __name__ == '__main__':
    unittest.main()
