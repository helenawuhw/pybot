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
  topic, number = shouldRespond(text)
  if (topic, number) != (None, None):
    list_ids = getPhotoIdsForTopic(topic, number)
    return [getPhotoUrlForId(photo_id) for photo_id in list_ids]


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
    topic = match.group(1).strip() or DEFAULT_BOMB_TOPIC
    number = int((match.group(3) or '').strip() or DEFAULT_BOMB_COUNT)
    return topic, number
  return None, None


"""
  Call the flickr API and return a list of photo ids corresponding to a specific topic
"""
def getPhotoIdsForTopic(topic, number):
  return parsePhotoIdsFromJsonResponse(getPhotoIdJsonForTopic(topic,number))


"""
  Call the flickr API and return the json response for a photo search on a topic
"""
def getPhotoIdJsonForTopic(topic, number):
  a = 'http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8ac641379dc965b3ffb0eb1ed4bf055a&tags='
  b = '&per_page='
  c = '&format=json&nojsoncallback=1'
  urled_topic = urllib2.quote(topic)
  complete_url = a + urled_topic + b + `number` + c
  apiCall = urllib2.urlopen(complete_url)
  return json.loads(apiCall.read())


"""
  Parse the json response to determine the list of ids for the photos
"""
def parsePhotoIdsFromJsonResponse(response):
  if not response['photos']['photo']:
    return None
  else:
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
  a = 'http://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=8ac641379dc965b3ffb0eb1ed4bf055a&photo_id='
  b = '&format=json&nojsoncallback=1'
  complete_url = a + id_number + b
  apiCall = urllib2.urlopen(complete_url)
  return json.loads(apiCall.read())


"""
  Parse the json response to figure out the right photo url
"""
def parsePhotoUrlFromJsonResponse(response):
  n = (len(response['sizes']['size']))
  return response['sizes']['size'][n/2]['source']
  