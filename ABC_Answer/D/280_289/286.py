N, X = map(int, input().split())
A, B = [], []
for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

A = [0] + A
B = [0] + B
dp = [[0] * (X+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
  for x in range(X+1):
    if dp[i-1][x] == 1:
      a = A[i]
      for b in range(B[i]+1):
        if x + a * b < X:
          dp[i][x + a * b] = 1
        elif x + a * b == X:
          print('Yes')
          exit()

print('No')
