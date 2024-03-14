def generateBase(baseArray, powerArray):
    baseString = ""
    # Array of dictionary holding the power alphabet as value fo
    '''
    List of dictionary holding the power letter as value for respective alphabet
    acting as key. This list stores only those alphabets in the base array which
    has variable power  
    '''
    stateNoforNArray = []
    for i in range(len(baseArray)):
        currentChar = baseArray[i]
        currentPower = powerArray[i]
        '''
        Checks if the current array element is a dictionary, if so the base string will be 
        formed by concatenating the alphabet least value of the respective variable power
        stored in the dictionary as value.
        '''
        if isinstance(currentPower, dict):
            powkey = list(currentPower)
            for i in range(currentPower[powkey[0]]):
                baseString += currentChar
            stateNoforNArray.append({"q"+str(len(baseString)) : currentChar})
        else:
            '''
            If not a dictionary, then the base string will be appended by the alphabet by 
            power number of times
            '''
            for i in range(currentPower):
                baseString += currentChar
    return baseString, stateNoforNArray