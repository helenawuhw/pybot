
import urllib2

"""
  Return the WMATA json response for the Courthouse metro stop
"""
def getJsonForCourthouse():
  function = urllib2.urlopen('http://api.wmata.com/StationPrediction.svc/json/GetPrediction/K01?api_key=ten3y6u8f6qdn5trz7am72jq')
  return function.read()



def time(response, direction, destination):
  n_trains = len(response['Trains'])
  if n_trains < 1:
    return ''  #returns None when there is no info about trains
  for i in range(0, n_trains):
    if response['Trains'][i]['Destination'] == destination:
        direction.append(i)
  return `min([int(response['Trains'][n]['Min']) for n in direction])`

"""
Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Westward (towards Clarendon / Vienna) (in minutes, as a string)
"""


def timeForNextWestTrain(wmataResponse):
  """
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Eastwarn (towards Rosslyn / New Carrolton) (in minutes, as a string)
"""
  west_trains = []
  return time(wmataResponse, west_trains, "Vienna")


def timeForNextEastTrain(wmataResponse):
  east_trains = []
  return time(wmataResponse, east_trains, "NewCrltn")



