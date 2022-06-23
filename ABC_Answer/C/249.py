import itertools
import sys
input = sys.stdin.readline
 
N, K = map(int, input().split())
xList = [input() for _ in range(N)]
 
numList = [i for i in range(N)]
result = 0
 
alphaList = [chr(i) for i in range(97, 97+26)]
alphaDict = {}
for alpha in alphaList:
  alphaDict[alpha] = 0
 
for i in range(K,N+1):
  for comb in itertools.combinations(numList, i):
    for j in list(comb):
      for x_char in xList[j]:
        try:
          alphaDict[x_char] += 1
        except KeyError:
          None
  
    cnt = 0
    for v in alphaDict.values():
      if v == K:
        cnt += 1
    
    if cnt > result:
      result = cnt
    
    for alpha in alphaList:
      alphaDict[alpha] = 0
    
print(result)