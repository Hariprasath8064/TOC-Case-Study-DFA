def generateStateArray():
  stateArray = [{"q0": ""}]
  return stateArray

def createState(state, stateArray):
  stateArray.append({state: ""})

def updateStateProp(state, newString, stateArray:list):
  for i in stateArray:
    if i == state:
      i[state] += newString

