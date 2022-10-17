from math import ceil

X, Y = map(int, input().split())

dif = Y - X
if dif > 0:
  print(ceil(dif/10))
else:
  print(0)
