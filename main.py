def getLanguage():
  n = int(input("no of alphabets: "))
  alphabetSet = []
  print(f"Enter {n} alphabets:")
  for _ in range(n):
    alphabetSet.append(input())
  return alphabetSet

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

if __name__ == "__main__":
  alphabetSet = getLanguage()
  baseArray, powerArray = generateBaseAndPowerArrays(alphabetSet)
  print(baseArray)
  print(powerArray)
    