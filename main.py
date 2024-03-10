import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA, completeDFAMatrix

if __name__ == "__main__":
  alphabetSet = getLanguage.getLanguage()
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)

  baseCase = generateBase.generateBase(baseArray, powerArray)

  (DFA_Matrix, stateArray) = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase)
  alphadict = {}
  for i in range(len(alphabetSet)):
    alphadict[i] = alphabetSet[i]

  DFA_Matrix = completeDFAMatrix.complete_DFA(DFA_Matrix, stateArray, alphadict)  
  print("Base Array: ", baseArray)
  print("Power Array: ", powerArray)
  print("Base String: ", baseCase)
  print("DFA_Matrix: ", DFA_Matrix)
  print("State_Array: ", stateArray)
  