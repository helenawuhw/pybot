import urllib2
import re
import json


"""
  Return the website json response for Chuck Norris jokes
"""
def getJsonForJokes():
  apiCall = urllib2.urlopen('http://api.icndb.com/jokes/random/')
  return json.loads(apiCall.read())


"""
  Returns the joke as a string without the parentheses 
"""
def getJoke():
  response = getJsonForJokes()
  start_index = response.find('"joke":')
  end_index = response.find('.", "categories": ["')
  return response[start_index + 9: end_index + 2]


"""
  Returns the joke as a string without the parentheses 
"""
def cnJokes(text):
  if re.findall('chuck norris', text, re.I):
    return getJoke()