## 模解のコードを C++ から python で書いた

from collections import defaultdict

def maxmum_same(R):
  R_Map = defaultdict(int)
  res = 0
  for i in range(len(R)):
    R_Map[R[i]] += 1
    res = max(res, R_Map[R[i]])
  return res


H, W = map(int, input().split())
P = []
for i in range(H):
  P.append(list(map(int, input().split())))

ans = 0
for i in range(1, 2**H):
  R = []
  for j in range(W):
    idx = -1
    flag = False
    for k in range(H):
      if ((i >> k) & 1):
        if idx == -1:
          idx = P[k][j]
        elif idx != P[k][j]:
          flag = True
    if flag == False:
      R.append(idx)
  
  cntH = 0
  cntW = maxmum_same(R)
  for j in range(H):
    if ((i >> j) & 1):
      cntH += 1
  ans = max(ans, cntH*cntW)

print(ans)