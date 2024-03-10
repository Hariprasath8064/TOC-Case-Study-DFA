import StateFunctions

def generateBaseDFA(alphabetSet, baseString):
    num_states = len(baseString) + 1
    num_symbols = len(alphabetSet)
    DFA_Matrix = [[" " for _ in range(num_symbols)] for _ in range(num_states)]   
    index_dict = {}
    stateArray = StateFunctions.generateStateArray()

    for i in range(len(alphabetSet)):
        index_dict[alphabetSet[i]] = i
    statechar = "q"
    stateprop = ""
    for i in range(len(baseString)):
        newState = statechar + str(i + 1)
        StateFunctions.createState(newState, stateArray)
        currentAlphabet = baseString[i]
        stateprop += currentAlphabet
        StateFunctions.updateStateProp(newState, stateprop, stateArray)
        DFA_Matrix[i][index_dict[currentAlphabet]] = newState
    return (DFA_Matrix, stateArray)