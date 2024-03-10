def generateStateArray():
  stateArray = [{"q0": ""}]
  return stateArray

def createState(state, stateArray):
  stateArray.append({state: ""})

def updateStateProp(state, newString, stateArray:list):
  for key, value in stateArray:
    if key == state:
      value += newString

