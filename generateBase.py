def generateBase(baseArray, powerArray):
    baseString = ""
    stateNoforNArray = []
    for i in range(len(baseArray)):
        currentChar = baseArray[i]
        currentPower = powerArray[i]
        if isinstance(currentPower, dict):
            powkey = list(currentPower)
            for i in range(currentPower[powkey[0]]):
                baseString += currentChar
            stateNoforNArray.append("q"+str(len(baseString)))
        else:
            for i in range(currentPower):
                baseString += currentChar
    return baseString, stateNoforNArray