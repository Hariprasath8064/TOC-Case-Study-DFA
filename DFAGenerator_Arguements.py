def arguementGenerator(stateArray, alphabetSet, finalStateArray, DFA_Matrix):
    '''
    State array is a list of dictionary which is converted into a list 
    then it is typacasted into set.
    '''
    new_state = [next(iter(state.keys())) for state in stateArray]
    new_state = set(new_state)

    new_input_symbols = set()
    for i in alphabetSet:
        new_input_symbols.add(i)
    
    new_final_state = set(finalStateArray)

    '''
    DFA Matrix is converted into a dictionary of dictionaries by the below code.
    '''    
    my_transitions = {}
    for i, state_transitions in enumerate(DFA_Matrix):
        state_name = "q" + str(i)
        my_transitions[state_name] = {} 

        for symbol_index, transition_state in enumerate(state_transitions):
            if symbol_index < len(alphabetSet):  
                symbol = alphabetSet[symbol_index] 
                my_transitions[state_name][symbol] = transition_state

    return (new_state, new_input_symbols, new_final_state, my_transitions)