import StateFunctions

def fillTrapStatesDFAMatrix(DFA_Matrix, i, j, currentAlphabet, baseString, stateArray, finalStateArray):
    currentState = "q" + str(i)
    if j < len(DFA_Matrix[0]) and i < len(baseString) and baseString[i-1] == currentAlphabet:
        DFA_Matrix[i][j] = currentState
    elif currentState in finalStateArray and baseString[-1] == currentAlphabet:
        DFA_Matrix[i][j] = currentState
    else:
        currentState = "q" + str(len(DFA_Matrix))
        StateFunctions.createState(currentState, stateArray)
        DFA_Matrix.append([])
        for k in range(len(DFA_Matrix[0])):
            DFA_Matrix[len(DFA_Matrix)-1].append(currentState)
        DFA_Matrix[i][j] = currentState
