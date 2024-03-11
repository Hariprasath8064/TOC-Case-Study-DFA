import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA, completeDFAMatrix
from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

if __name__ == "__main__":
  alphabetSet = getLanguage.getLanguage()
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)
  alphadict = {}
  finalStateArray = []
  intermediateNArray = []
  baseCase, intermediateNArray = generateBase.generateBase(baseArray, powerArray)

  (DFA_Matrix, stateArray) = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase, finalStateArray)
  for i in range(len(alphabetSet)):
    alphadict[i] = alphabetSet[i]

  DFA_Matrix = completeDFAMatrix.complete_DFA(DFA_Matrix, stateArray, alphadict, baseCase, finalStateArray, intermediateNArray)  
  print("Base Array: ", baseArray)
  print("Power Array: ", powerArray)
  print("intermediate Array: ", intermediateNArray)
  print("Base String: ", baseCase)
  print("DFA_Matrix: ")
  for i in DFA_Matrix:
    print(i)
  print("State_Array: ", stateArray)

  new_state = set()
  for state in stateArray:
    for key in state.keys():
      new_state.add(key)

  new_input_symbols = set()
  for i in alphabetSet:
    new_input_symbols.add(i)

  new_initial_state = 'q0'
  print("Final State: ", finalStateArray)
  new_final_state = set(finalStateArray)

  my_transitions = {}

  # Loop through each state's transitions in the DFA matrix
  for i, state_transitions in enumerate(DFA_Matrix):
      state_name = f'q{i}'  # Generate state name dynamically based on index
      my_transitions[state_name] = {}  # Initialize a new dictionary for this state's transitions
      
      # Map each alphabet symbol to the corresponding transition state from the matrix
      for symbol_index, transition_state in enumerate(state_transitions):
          if symbol_index < len(alphabetSet):  # Check to avoid index out of range
              symbol = alphabetSet[symbol_index]  # Get the symbol from the alphabet set
              my_transitions[state_name][symbol] = transition_state  # Assign the transition state

  # Now 'transitions' contains your DFA in the desired format
  print("Transitions: ", my_transitions)

  new_dfa = VisualDFA(
    states=new_state,
    input_symbols=new_input_symbols,
    transitions=my_transitions,
    initial_state=new_initial_state,
    final_states=new_final_state,
  )
  new_dfa.table
  new_dfa.show_diagram()

  