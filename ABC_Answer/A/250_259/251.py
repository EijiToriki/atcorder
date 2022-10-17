S = input()
 
outputS = S
 
for i in range(6):
  outputS += S
  if len(outputS) == 6:
    break
 
print(outputS)