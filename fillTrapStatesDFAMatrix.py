import StateFunctions

def fillTrapStatesDFAMatrix(DFA_Matrix, i, j, currentAlphabet, baseString, stateArray, finalStateArray, intermediateNArray):
  currentState = "q" + str(i)

  if j < len(DFA_Matrix[0]) and i < len(baseString) and (i >= 0 and baseString[i] == currentAlphabet):
    DFA_Matrix[i][j] = currentState

  elif any(state_dict.get(currentState) == currentAlphabet for state_dict in intermediateNArray):
    DFA_Matrix[i][j] = currentState

  else:
    flag = 0
    for state in stateArray:
      for key in state:
        if state[key] == "trap":
          DFA_Matrix[i][j] = key
          flag = 1
          break
    if flag == 0:
      currentState = "q" + str(len(DFA_Matrix))
      StateFunctions.createState(currentState, stateArray)
      StateFunctions.updateStateProp(currentState, "trap", stateArray)
      DFA_Matrix.append([])
      for k in range(len(DFA_Matrix[0])):
        DFA_Matrix[len(DFA_Matrix) - 1].append(currentState)
      DFA_Matrix[i][j] = currentState