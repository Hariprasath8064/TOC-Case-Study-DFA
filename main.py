import generateBase, getLanguage, generateBaseAndPowerArray

if __name__ == "__main__":
  alphabetSet = getLanguage.getLanguage()
  baseArray, powerArray = generateBaseAndPowerArray.generateBaseAndPowerArrays(alphabetSet)

  baseCase = generateBase.generateBase(baseArray, powerArray)
  print(baseCase)
    