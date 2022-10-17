import sys

N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
  for j in range(i+1, N):
    if A[i][j] == 'W':
      if A[j][i] != 'L':
        print('incorrect')
        sys.exit()
    if A[i][j] == 'D':
      if A[j][i] != 'D':
        print('incorrect')
        sys.exit()
    if A[i][j] == 'L':
      if A[j][i] != 'W':
        print('incorrect')
        sys.exit()

print('correct')