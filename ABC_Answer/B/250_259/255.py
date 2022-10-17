import math
import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []

for _ in range(N):
  x,y = map(int, input().split())
  X.append(x)
  Y.append(y)

xlight = []
ylight = []

for a in A:
  xlight.append(X[a-1])
  ylight.append(Y[a-1])

RList = []

for x,y in zip(X,Y):
  Rmin = sys.maxsize  ## その人にとっての最少距離を格納する
  for xl, yl in zip(xlight,ylight):
    r = (x-xl)*(x-xl) + (y-yl)*(y-yl)
    if Rmin > r:
      Rmin = r
  RList.append(Rmin)

print(math.sqrt(max(RList)))