N, M, K = map(int, input().split())

result = 0
dp = [[0] * (K+1) for i in range(N+1)]

dp[0][0] = 1

for i in range(0,N):
  for j in range(K+1):
    for k in range(1,M+1):
      if j+k <= K:
        dp[i+1][j+k] += dp[i][j]

for dpK in dp[N]:
  result += dpK

print(result%998244353)