from math import gcd

N = int(input())
XY = []
for _ in range(N):
  x, y = map(int, input().split())
  XY.append([x, y])

magic = set()
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    X, Y = XY[i][0]-XY[j][0], XY[i][1]-XY[j][1]
    g = gcd(X, Y)
    magic.add((X // g, Y // g))

print(len(magic))