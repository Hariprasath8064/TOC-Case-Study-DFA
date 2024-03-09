def getLanguage():
  n = int(input("no of alphabets: "))
  alphabetSet = []
  print(f"Enter {n} alphabets:")
  for _ in range(n):
    alphabetSet.append(input())
  return alphabetSet
