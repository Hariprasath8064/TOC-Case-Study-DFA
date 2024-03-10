import generateBase, getLanguage, generateBaseAndPowerArray, generateBaseDFA

if __name__ == "__main__":
  alphabetSet = getLanguage.getLanguage()
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)

  baseCase = generateBase.generateBase(baseArray, powerArray)
  print(baseCase)

  DFA_Matrix = generateBaseDFA.generateBaseDFA(alphabetSet, baseCase)
  print(DFA_Matrix)
    