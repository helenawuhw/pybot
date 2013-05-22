


"""
  Return True if we should respond to the message, False otherwise.
"""
def shouldRespond(text):
    return re.findall('chuck norris', message['text'], re.I) is not None #PERGUNTAR



"""
  Return the website json response for Chuck Norris jokes
"""
def getJsonForJokes():
  apiCall = urllib2.urlopen('http://api.icndb.com/jokes/random/')
  return apiCall.read()




def cnJokes(text):
  if re.findall('chuck norris', message['text'], re.I):
    return 'hey did you that Guarapo is 7th most famous guacamole bar in the mid-atlantic region?'