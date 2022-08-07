N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for n in range(N):
  for w in range(W+1):
    dp[n+1][w] = dp[n][w]
  for w in range(W+1):
    if w + wv[n][0] <= W:
      dp[n+1][w+wv[n][0]] = max(dp[n][w+wv[n][0]], dp[n][w] + wv[n][1])
    
print(max(dp[N]))