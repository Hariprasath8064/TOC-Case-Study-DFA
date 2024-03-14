def getLanguage():
  '''
  This module takes care of getting alphabet set input
  from the user and stores it in list for further reference
  '''
  n = int(input("no of alphabets: "))
  alphabetSet = []
  print(f"Enter {n} alphabets:")
  for _ in range(n):
    alphabetSet.append(input())
  return alphabetSet
