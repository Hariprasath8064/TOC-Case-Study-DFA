import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA, completeDFAMatrix

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
  