def complete_DFA(DFA_Matrix, stateArray, alphadict):
    for i in range(len(DFA_Matrix)):
        for j in range(len(DFA_Matrix[0])):
            if DFA_Matrix[i][j] == ' ':
                currentState = "q" + str(i)
                currentStateProperty = ""
                for state in stateArray:
                    if currentState in state:
                        currentStateProperty += state[currentState]
                print(currentStateProperty, " for Current State: ", currentState)
                transchar = alphadict[j]
                expectedProperty = currentStateProperty + transchar
                flag = 0
                for state in stateArray:
                    for key in state:
                        if state[key] == expectedProperty:
                            flag = 1
                            DFA_Matrix[i][j] = key
                            break
                    if flag:
                        break
    return DFA_Matrix
