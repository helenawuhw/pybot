import urllib2
import re
import json

"""
  Return the response for the text or None if we don't want to respond.

  Example:
    handleMessage('I am going to the moon') == None

    handleMessage('obot show me metro') == the response with the metro times
"""
def handleMessage(text):
  if shouldRespond(text):
    w = getJsonForCourthouse()
    resp =    formatTime("Vienna", timeForNextTrainToV(w)) + '\n' + \
              formatTime("New Carrolton", timeForNextTrainToNC(w)) + '\n' + \
              formatTime("Largo", timeForNextTrainToL(w))
    return resp
  else:
    return None


"""
  Return a string describing the time for the next train to a destination

  Example:
    formatTime('Vienna', '[6]') == 'The next train to Vienna is in 6 minutes'

    formatTime('New Carrolton', '[1,10]') == 'The next trains to New Carrolton are 1 and 10 minutes minutes'

    formatTime('Largo', None) == 'There is no scheduled train going to Largo'
"""
def formatTime(destination, times):
  if times is None:
    return "There is no scheduled train going to " + destination
  if len(times) == 1:
    return "The next train to " + destination + " is in " + `times[0]` + " minutes"
  else:
    return "The next trains to " + destination + " are in " + `times[0]` + " and " + `times[1]` + " minutes"
  

"""
  Return True if we should respond to the message, False otherwise.
"""
def shouldRespond(text):
  return re.search(r'^obot\s*show\s*me\s*metro', text) is not None  
  
"""
  Return the WMATA json response for the Courthouse metro stop
"""
def getJsonForCourthouse():
  apiCall = urllib2.urlopen('http://api.wmata.com/StationPrediction.svc/json/GetPrediction/K01?api_key=ten3y6u8f6qdn5trz7am72jq')
  return json.loads(apiCall.read())


"""
  Return the minimum time for the next train to destination (Vienna, New Carrolton or Largo) to arrive in a string
"""
def time(response, destination):
  indicies = []
  n_trains = len(response['Trains'])
  if n_trains < 1:
    return None  #returns None when there is no info about trains
  for i in range(n_trains):
    if response['Trains'][i]['Destination'] == destination:
        indicies.append(i)
  minutes_list = [response['Trains'][n]['Min'] for n in indicies if response['Trains'][n]['Min'].isdigit()]
  ints = [int(x) for x in minutes_list]
  if len(minutes_list) == 1:
    return [min(ints)]
  if len(minutes_list) > 1:
    ints.sort()
    return ints[:2]
  else:
    return None


"""
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Westward (towards Clarendon / Vienna) (in minutes, as a string)
"""
def timeForNextTrainToV(wmataResponse):
  return time(wmataResponse, "Vienna")


"""
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Eastwarn (towards Rosslyn / New Carrolton) (in minutes, as a string)
"""
def timeForNextTrainToNC(wmataResponse):
  return time(wmataResponse, "NewCrltn")


"""
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Eastwarn (towards Rosslyn / Largo Town Center) (in minutes, as a string)
  if no trains to Largo, return ''
"""
def timeForNextTrainToL(wmataResponse):
    return time(wmataResponse, "Largo")


