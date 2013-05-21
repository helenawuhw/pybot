
import urllib2

"""
  Return the WMATA json response for the Courthouse metro stop
"""
def getJsonForCourthouse():
  function = urllib2.urlopen('http://api.wmata.com/StationPrediction.svc/json/GetPrediction/K01?api_key=ten3y6u8f6qdn5trz7am72jq')
  return function.read()

"""
Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Westward (towards Clarendon / Vienna) (in minutes, as a string)
"""


def timeForNextWestTrain(wmataResponse):
  """
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Eastwarn (towards Rosslyn / New Carrolton) (in minutes, as a string)
"""

  n_trains = len(wmataResponse['Trains'])
  if n_trains < 1:
    return ''  #returns None when there is no info about trains
  
  i = 0 #not sure if i need this, check later
  west_trains = []
  for i in range(0, n_trains):
    if wmataResponse['Trains'][i]['Destination'] == "Vienna":
        west_trains.append(i)
    i =+ i
  minutes = [int(wmataResponse['Trains'][n]['Min']) for n in west_trains]
  min_minutes = min(minutes)
  return `min_minutes`


def timeForNextEastTrain(wmataResponse):  
  n_trains = len(wmataResponse['Trains'])
  if n_trains < 1:
    return ''  #returns None when there is no info about trains
  
  i = 0 #not sure if i need this, check later
  east_trains = []
  for i in range(0, n_trains):
    if wmataResponse['Trains'][i]['Destination'] == "NewCrltn":
        east_trains.append(i)
    i =+ i
  minutes = [int(wmataResponse['Trains'][n]['Min']) for n in east_trains]
  min_minutes = min(minutes)
  return `min_minutes`
