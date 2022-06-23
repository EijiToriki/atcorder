import sys

N = int(input())
X = []
Y = []

for _ in range(N):
  x,y = map(int, input().split())
  X.append(x)
  Y.append(y)

S = input()

rightDict = {}  ## key : y座標，value : そのy座標で一番右にいる人のx座標
leftDict = {}   ## key : y座標，value : そのy座標で一番左にいる人のx座標



for i in range(N):
  if S[i] == 'L':
    if Y[i] not in rightDict:   # 初期登録
      rightDict[Y[i]] = X[i]
    else:    
      if rightDict[Y[i]] < X[i]:
        rightDict[Y[i]] = X[i] 

  if S[i] == 'R':
    if Y[i] not in leftDict:    # 初期登録
      leftDict[Y[i]] = X[i]
    else:
      if S[i] == 'R':
        if leftDict[Y[i]] > X[i]:
          leftDict[Y[i]] = X[i]
  
  if Y[i] in rightDict and Y[i] in leftDict:
    if rightDict[Y[i]] > leftDict[Y[i]]:
      print('Yes')
      sys.exit()

print('No')
