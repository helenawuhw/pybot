import unittest
import bomb
import json

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.getPhotosResponse = json.loads(open('fixtures/bomb-get-photos.json', 'r').read())
        self.getSizesResponse = json.loads(open('fixtures/bomb-get-sizes.json', 'r').read())

    def test_shouldRespond_emptyString(self):
        self.assertEquals((None, None), bomb.shouldRespond(''))

    def test_shouldRespond_notRelevant(self):
        self.assertEquals((None, None), bomb.shouldRespond('obot is going to the moon'))

    def test_shouldRespond_noTopic(self):
        self.assertEquals((bomb.DEFAULT_BOMB_TOPIC, "10"), bomb.shouldRespond('obot bomb 10'))

    def test_shouldRespond_noCount(self):
        self.assertEquals(('dangerzone', bomb.DEFAULT_BOMB_COUNT), bomb.shouldRespond('obot dangerzone bomb'))

    def test_shouldRespond_countAndTopic(self):
        self.assertEquals(('loggins', "8"), bomb.shouldRespond('obot loggins bomb 8'))

    def test_shouldRespond_topicWithSpaces(self):
        self.assertEquals(('danger zone', "8"), bomb.shouldRespond('obot danger zone bomb 8'))

    def test_parsePhotoIdsFromJsonResponse(self):
        self.assertEquals(
          ['8803736756', '8793060167', '8803641088', '8803203226', '8803202868'], 
          bomb.parsePhotoIdsFromJsonResponse(self.getPhotosResponse)
        )

    def test_parsePhotoUrlFromJsonResponse(self):
        self.assertEquals(
          # Feel free to change this expected response to something that makes more sense
          r'http://farm9.staticflickr.com/8120/8792081739_9538871ce5.jpg',
          bomb.parsePhotoUrlFromJsonResponse(self.getSizesResponse)
        )

if __name__ == '__main__':
    unittest.main()