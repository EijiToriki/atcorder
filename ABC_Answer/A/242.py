A, B, C, X = map(int, input().split())

if A >= X:
  print(1)
elif B < X:
  print(0)
else:
  target = B - A
  print(C/target)