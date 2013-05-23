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
def getJoke(response):
  return response["value"]['joke']


"""
  Returns the joke as a string without the parentheses 
"""
def handleMessage(text):
  if re.findall('chuck norris', text, re.I):
    return getJoke(getJsonForJokes())