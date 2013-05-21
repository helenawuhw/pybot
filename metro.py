

import urllib2

"""
  Return the WMATA json response for the Courthouse metro stop
"""
def getJsonForCourthouse():
  function = urllib2.urlopen('http://api.wmata.com/StationPrediction.svc/json/GetPrediction/K01?api_key=ten3y6u8f6qdn5trz7am72jq')
  return function.read()


"""
  Return the minimum time for the next train to destination (Vienna, New Carrolton or Largo) to arrive in a string
"""
def time(response, destination):
  list_indicies = []
  n_trains = len(response['Trains'])
  if n_trains < 1:
    return ''  #returns None when there is no info about trains
  for i in range(0, n_trains):
    if response['Trains'][i]['Destination'] == destination:
        list_indicies.append(i)
  minutes_list = [response['Trains'][n]['Min'] for n in list_indicies if response['Trains'][n]['Min'] != '']
  if len(minutes_list) > 1:
    int_list = [int(x) for x in minutes_list]
    return `min(int_list)`
  else:
    return ''


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
  if no trains to Largo, return "No trains to Largo"
"""
def timeForNextTrainToL(wmataResponse):
  if time(wmataResponse, "Largo"):
    return time(wmataResponse, "Largo")
  else:
    return "No trains to Largo"
  


