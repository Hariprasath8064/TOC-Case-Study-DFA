def generateStateArray():
  stateArray = [{"q0": ""}]
  return stateArray

def createState(state, stateArray):
  stateArray.append({state: ""})

def updateStateProp(stateName, newString, stateArray):
    for state in stateArray:
        if stateName in state:
            state[stateName] += newString


