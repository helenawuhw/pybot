"""
  Return the WMATA json response for the Courthouse metro stop
"""
def getJsonForCourthouse():
  pass

"""
Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Westward (towards Clarendon / Vienna) (in minutes, as a string)
"""


def timeForNextWestTrain(wmataResponse):
  """
  Argument: the return value of getJsonForCourthouse()

  Return the time until the next train leaves Eastwarn (towards Rosslyn / New Carrolton) (in minutes, as a string)
"""

  return ((wmataResponse['Trains'])[1])['Min']
  

  
  

def timeForNextEastTrain(wmataResponse):
  #RASCUNHO QUE FUNCIONA
  
  #print `wmataResponse`
  ##print 'hi'
  ##print wmataResponse['Trains']
  ##print 'hello'
  #inside_dict = wmataResponse['Trains']
  #first_element = inside_dict[0]
  ##print first_element
  ##print 'oi'
  #minutes = first_element['Min']
  #
  ##print minutes
  #return minutes
  
    return ((wmataResponse['Trains'])[0])['Min']