inStr = input()

lowFlag = 0
highFlag = 0
charList = []
result = 0

for char in inStr:
  if char.islower() and lowFlag == 0:
    result = result + 1
    lowFlag = 1
  if char.isupper() and highFlag == 0:
    result = result + 1
    highFlag = 1
  charList.append(char)

if len(set(charList)) == len(inStr):
  result = result + 1

if result == 3:
  print("Yes")
else:
  print("No")
