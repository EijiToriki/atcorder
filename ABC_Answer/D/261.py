N, M = map(int, input().split())
X = [0] + list(map(int, input().split()))

b = [0 for _ in range(N+1)]
for i in range(M):
  c, y = map(int, input().split())
  b[c] = y

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, i+1):
    dp[i][j] = dp[i-1][j-1] + X[i] + b[j]

  dp[i][0] = 0
  for j in range(i):
    dp[i][0] = max(dp[i][0], dp[i-1][j])
    
ans = 0
for i in range(N+1):
  ans = max(ans, dp[N][i])

print(ans)