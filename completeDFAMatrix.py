# Importing Necessary Modules
import fillTrapStatesDFAMatrix

def complete_DFA(DFA_Matrix, stateArray, alphadict, baseString, finalStateArray, intermediateNArray):

    '''
    Completes DFA Matrix by searching for empty transition cells in the matrix
    Uses Logic of searching for state which has expected state property
    If no state is found uses the module of fillTrapStatesDFAMatrix for filling the respective transition
    '''

    for i in range(len(DFA_Matrix)):
        for j in range(len(DFA_Matrix[0])):
            # Searches for DFA Matrix Cell where its not yet filled
            if DFA_Matrix[i][j] == ' ':
                currentState = "q" + str(i)
                currentStateProperty = ""
                # Getting the State Property of the current cell from the StateArray
                for state in stateArray:
                    if currentState in state:
                        currentStateProperty += state[currentState]
                transchar = alphadict[j]

                # Generating Expected State Property by concatenating Current State's property with the respective transition Alphabet
                expectedProperty = currentStateProperty + transchar

                # flag denotes the status of respective cell in the DFA Matrix [Filled or Empty]
                flag = 0
                for state in stateArray:
                    for key in state:
                        if state[key] == expectedProperty:
                            flag = 1
                            DFA_Matrix[i][j] = key
                            break
                    if flag:
                        break

                '''
                If no state is found in the state array with expected property then the respective state 
                transtion would have two possibilities either to transition to a trap state or to itself
                The decision for that transition will be made by fillTrapStatesDFAMatrix Module
                '''
                if flag == 0:
                    fillTrapStatesDFAMatrix.fillTrapStatesDFAMatrix(DFA_Matrix, i, j, transchar, baseString, stateArray, finalStateArray, intermediateNArray)
    # Return Completed DFA Matrix
    return DFA_Matrix
