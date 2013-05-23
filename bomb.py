import urllib2
import re
import json
import random

"""
Custom photo bombing via the flickr api
"""


"""
  Return a response for `text` if we want to respond; otherwise None
"""
def handleMessage(text):
  s = shouldRespond(text)
  if s != (None, None):
    topic, number = s
    list_ids = getPhotoIdsForTopic(topic)
    return ','.join([getPhotoUrlForId(photo_id) for photo_id in list_ids])


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
  match = re.search(r'obot ((\w* )*)bomb( (\d*))?', text)
  if match is not None:
    topic = match.group(1)
    number = match.group(3)
    if number is None:
      return topic.strip(), DEFAULT_BOMB_COUNT
    if topic.strip() == '':
      return DEFAULT_BOMB_TOPIC, number.strip()
    if topic.strip() == '' and number is None:
      return DEFAULT_BOMB_TOPIC, DEFAULT_BOMB_COUNT
    else:
      return topic.strip(), number.strip()
  else:
    return None, None


"""
  Call the flickr API and return a list of photo ids corresponding to a specific topic
"""
def getPhotoIdsForTopic(topic):
  return parsePhotoIdsFromJsonResponse(getPhotoIdJsonForTopic(topic))


"""
  Call the flickr API and return the json response for a photo search on a topic
"""
def getPhotoIdJsonForTopic(topic):
  urled_topic = urllib2.quote(topic)
  apiCall = urllib2.urlopen('http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=767cf3bb0a87cfafaf46bbebda08e646&tags=' + urled_topic + '&format=json&nojsoncallback=1')
  return json.loads(apiCall.read())


"""
  Parse the json response to determine the list of ids for the photos
"""
def parsePhotoIdsFromJsonResponse(response):
  return [photo['id'] for photo in response['photos']['photo']]


"""
  Call the flickr API to get the image url for a photo id
"""
def getPhotoUrlForId(id_number):
  return parsePhotoUrlFromJsonResponse(getPhotoUrlJsonForId(id_number))
 

"""
  Call the flickr API to get the json photo url response for a specific photo id
"""
def getPhotoUrlJsonForId(id_number):
  apiCall = urllib2.urlopen('http://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=8ac641379dc965b3ffb0eb1ed4bf055a&photo_id=' + id_number + '&format=json&nojsoncallback=1')
  return json.loads(apiCall.read())


"""
  Parse the json response to figure out the right photo url
"""
def parsePhotoUrlFromJsonResponse(response):
  n = (len(response['sizes']['size']))
  return response['sizes']['size'][n/2]['source']
  