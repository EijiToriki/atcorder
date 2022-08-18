from collections import defaultdict


N = int(input())
L = []
for _ in range(N):
  L.append(list(map(int, input().split())))
  
arrayDict = defaultdict(int)

for i in range(N):
  arrayDict[''.join(str(L[i][1:]))] += 1

print(len(arrayDict.keys()))
