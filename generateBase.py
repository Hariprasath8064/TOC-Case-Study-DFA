def generateBase(baseArray, powerArray):
    baseString = ""
    for i in range(len(baseArray)):
        currentChar = baseArray[i]
        currentPower = powerArray[i]
        if isinstance(currentPower, dict):
            powkey = list(currentPower)
            for i in range(currentPower[powkey[0]]):
                baseString += currentChar
        else:
            for i in range(currentPower):
                baseString += currentChar
    return baseString


baseArray = ['a', 'a', 'a', 'b']
powerArray = [1, 1, 1, {'n': 0}]

print(generateBase(baseArray, powerArray))
