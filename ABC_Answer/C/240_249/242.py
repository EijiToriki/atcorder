N = int(input())
mod = 998244353

dp = [[0] * 10 for _ in range(N+1)]

for j in range(1,10):
  dp[1][j] = 1

for i in range(2,N+1):
  dp[i][1] = (dp[i-1][1] + dp[i-1][2])%mod
  dp[i][9] = (dp[i-1][8] + dp[i-1][9])%mod
  for j in range(2,9):  
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    dp[i][j] %= mod

result = 0
for i in dp[N]:
  result += i
  result %= mod

print(result)