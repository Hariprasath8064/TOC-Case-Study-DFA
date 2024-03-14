import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA, completeDFAMatrix, DFAGenerator_Arguements
from graphviz import Digraph

if __name__ == "__main__":
  # Initializations
  dot = Digraph()
  alphadict = {}
  finalStateArray = []
  intermediateNArray = []

  # Get Language Set
  alphabetSet = getLanguage.getLanguage()

  # Get Base Array and Power Array
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays()
  baseCase, intermediateNArray = generateBase.generateBase(baseArray, powerArray)

  # Get Generated Base DFA Matrix
  (DFA_Matrix, stateArray) = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase, finalStateArray)
  for i in range(len(alphabetSet)):
    alphadict[i] = alphabetSet[i]

  # Complete the DFA Matrix 
  DFA_Matrix = completeDFAMatrix.complete_DFA(DFA_Matrix, stateArray, alphadict, baseCase, finalStateArray, intermediateNArray)  

  # Print The Language Properties
  print("------------------------------------------")
  print("Language Properties: ")
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


  # Convert all Data to Specific form   
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

  # Draw Arrow to the Initial State
  dot.attr('node', shape = "none")
  dot.node("")
  dot.edge("", "q0")

  # Design Seperate states based on their status [Final or Non-Final]
  for state in new_state:
      if state in new_final_state:
          dot.node(state, shape='doublecircle')
      else:
          dot.node(state,shape="circle")

  # Draw respective edges between the states by referring to the transition table 
  for state, transitions in my_transitions.items():
      for symbol, next_state in transitions.items():
          dot.edge(state, next_state, label=symbol)
  dot.render('dfa_graph', format='png', view=True)

  