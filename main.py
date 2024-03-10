import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA

if __name__ == "__main__":
  alphabetSet = getLanguage.getLanguage()
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)

  baseCase = generateBase.generateBase(baseArray, powerArray)

  (DFA_Matrix, stateArray) = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase)
  print("Base Array: ", baseArray)
  print("Power Array: ", powerArray)
  print("Base String: ", baseCase)
  print("DFA_Matrix: ", DFA_Matrix)
  print("State_Array: ", stateArray)
  