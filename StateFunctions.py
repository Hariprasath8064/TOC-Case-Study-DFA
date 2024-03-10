def generateStateArray():
  stateArray = [{"q0": ""}]
  return stateArray

def createState(state, stateArray):
  stateArray.append({state: ""})

def updateStateProp(state, newString, stateArray:list):
  for state in stateArray:
    for key, value in state.items():
      if key == state:
        value += newString

