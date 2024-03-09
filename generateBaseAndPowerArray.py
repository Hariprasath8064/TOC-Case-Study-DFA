def generateBaseAndPowerArrays(alphabetSet):
  baseArray = []
  powerArray = []
  print("Enter base and power:")
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
