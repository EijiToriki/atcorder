import sys

N = int(input())

ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

min_time = sys.maxsize 

for i in range(N):
  for j in range(N):
    enter = A[i]
    exit = B[j]
    time = 0
    for k in range(N):
      time += abs(A[k]-enter) + abs(B[k]-A[k]) + abs(B[k]-exit)
    if time < min_time:
      min_time = time

print(min_time)
