import StateFunctions

def fillTrapStatesDFAMatrix(DFA_Matrix:list[list[str]], i:int, j:int, currentAlphabet:str, baseString:str, stateArray:list[dict], finalStateArray, intermediateNArray:list[dict]):

  '''
  This function iterates through the DFA matrix and determines the transitions, deciding whether to transition to a trap state or remain in the current state.
  '''

  # current row in the transition table is recived as parameter i -> now converted to a string name for representing state
  currentState = "q" + str(i)

  # if the currentAlphabet equals the alphabet in the basearray then transition to the same state
  if j < len(DFA_Matrix[0]) and i < len(baseString) and (i >= 0 and baseString[i] == currentAlphabet):
    DFA_Matrix[i][j] = currentState

  # if not then a special array called intermediateNArray is maintened - which stores the state where there was power n notation - and we check if the current state is present in the list of dictionaries, if yes then transition happens to the same state
  elif any(state_dict.get(currentState) == currentAlphabet for state_dict in intermediateNArray):
    DFA_Matrix[i][j] = currentState

  # if both these cases fail, then it means the transition needs to be a trap state, so we check if already a trap state is there - if yes, go to it else create a new trap state
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