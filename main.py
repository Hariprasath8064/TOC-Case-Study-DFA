import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA, completeDFAMatrix, DFAGenerator_Arguements
from graphviz import Digraph

if __name__ == "__main__":
  # Initializations
  dot = Digraph()

  # Get Language Set
  alphabetSet = getLanguage.getLanguage()

  # Get Base Array and Power Array
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)
  alphadict = {}
  finalStateArray = []
  intermediateNArray = []
  baseCase, intermediateNArray = generateBase.generateBase(baseArray, powerArray)

  # Get Generated Base DFA Matrix
  (DFA_Matrix, stateArray) = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase, finalStateArray)
  for i in range(len(alphabetSet)):
    alphadict[i] = alphabetSet[i]

  # Complete the DFA Matrix 
  DFA_Matrix = completeDFAMatrix.complete_DFA(DFA_Matrix, stateArray, alphadict, baseCase, finalStateArray, intermediateNArray)  
  print("Base Array: ", baseArray)
  print("Power Array: ", powerArray)
  print("intermediate Array: ", intermediateNArray)
  print("Base String: ", baseCase)

  print("-----------------------------------------")
  print("State Array with Properties")
  print("-----------------------------------------")
  for state_dict in stateArray:
    for state, value in state_dict.items():
      print(f"{state}: \"{value}\"")
  print("------------------------------------------")



  (new_state, new_input_symbols, new_final_state, my_transitions) = DFAGenerator_Arguements.arguementGenerator(stateArray, alphabetSet, finalStateArray, DFA_Matrix)
  new_initial_state = 'q0'

  print("-----------------------------------------")
  print("Transition Table:")
  print("-----------------------------------------")
  for state, trans in my_transitions.items():
    print(f"{state}: ", end="")
    transitions_str = ", ".join([f"{symbol} -> {dest}" for symbol, dest in trans.items()])
    print(transitions_str)
  print("-----------------------------------------")


  # Generate Each Node
  for state in new_state:
      if state in new_final_state:
          dot.node(state, shape='doublecircle')
      else:
          dot.node(state)

  # Connect all Nodes with respective Edges from DFA_Matrix
  for state, transitions in my_transitions.items():
      for symbol, next_state in transitions.items():
          dot.edge(state, next_state, label=symbol)
  dot.render('dfa_graph', format='png', view=True)

  