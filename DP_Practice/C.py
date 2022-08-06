N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N+1)]

for i in range(N):
  abc = list(map(int, input().split()))
  for j in range(3):
    for k in range(3):
      if j == k:
        continue
      else:
        dp[i+1][k] = max(dp[i+1][k], dp[i][j]+abc[k])

print(max(dp[N]))
