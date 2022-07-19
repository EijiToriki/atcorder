from math import sqrt


N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

max_length = 0
for i in range(N):
  for j in range(i+1,N):
    length = (x[j]-x[i])**2 + (y[j]-y[i])**2
    if max_length < length:
      max_length = length

print(sqrt(max_length))
