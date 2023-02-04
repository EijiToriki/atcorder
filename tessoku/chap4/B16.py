N = int(input())
H = [0] + list(map(int, input().split()))
dp = [float('inf')] * (N+1)
dp[0], dp[1] = 0, 0
dp[2] = abs(H[2]-H[1])

for i in range(3, N+1):
  dp[i] = min(dp[i], dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

print(dp[N])
