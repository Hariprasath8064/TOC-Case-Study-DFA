def getLanguage():
  baseArray = []
  powerArray = []
  while True:
    base = input()
    if base == "end":
      break
    power = input()
    if base.isalpha():
      baseArray.append(base)
    if power.isnumeric():
      powerArray.append(int(power))
    else:
      lowerBound = int(input())
      powerArray.append({power: lowerBound})
  return (baseArray, powerArray)

if __name__ == "__main__":
  baseArray, powerArray = getLanguage()
  print(baseArray)
  print(powerArray)
    