N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf') for _ in range((10**3)*N+1)] for _ in range(N+1)]

dp[0][0] = 0

for n in range(N):
  for v in range(10**3*N+1):
    if v-wv[n][1] >= 0:
      dp[n+1][v] = min(dp[n][v], dp[n][v-wv[n][1]] + wv[n][0])
    dp[n+1][v] = min(dp[n+1][v], dp[n][v])
    
res = 0
for i in range(len(dp[N])):
  if dp[N][i] <= W:
    res = i

print(res)
