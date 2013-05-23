"""
Custom photo bombing via the flickr api
"""

"""
  Return a response for `text` if we want to respond; otherwise None
"""
def handleMessage(text):
  pass


"""
  The count of photos to bomb if the user doesn't specify anything
"""
DEFAULT_BOMB_COUNT = 5

"""
  The default photo topic to bomb if the user doesn't specify anything
"""
DEFAULT_BOMB_TOPIC = 'kenny loggins'

"""
  Return a tuple of (topic, count) if we should respond; otherwise (None, None)

  Examples
    shouldRespond('') == (None, None)
    shouldRespond('obot let's go to the moon') == (None, None)
    shouldRespond('obot pony bomb 15') == ('pony', 15)
    shouldRespond('obot my little pony bomb 20') == ('my little pony', 20)
    shouldRespond('obot loggins bomb') == ('loggins', DEFAULT_BOMB_COUNT)
    shouldRespond('obot bomb 13') == (DEFAULT_BOMB_TOPIC, 13)
"""
def shouldRespond(text):
  pass

"""
  Call the flickr API and return a list of photo ids corresponding to a specific topic
"""
def getPhotoIdsForTopic(topic):
  pass

"""
  Call the flickr API and return the json response for a photo search on a topic
"""
def getPhotoIdJsonForTopic(topic):
  pass

"""
  Parse the json response to determine the list of ids for the photos
"""
def parsePhotoIdsFromJsonResponse(response):
  pass

"""
  Call the flickr API to get the image url for a photo id
"""
def getPhotoUrlForId(id):
  pass

"""
  Call the flickr API to get the photo url response for a specific photo id
"""
def getPhotoUrlJsonForId(id):
  pass

"""
  Parse the json response to figure out the right photo url
"""
def parsePhotoUrlFromJsonResponse(response):
  pass