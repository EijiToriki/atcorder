N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

dp = [[-float('INF')]*(N+1) for _ in range(M+1)]

dp[1][1] = A[1]
for i in range(2, N-M+2):
    dp[1][i] = max(dp[1][i-1], A[i])

for i in range(2, M+1):
    for j in range(i, N-M+i+1):
        val = dp[i-1][j-1] + i*A[j]
        dp[i][j] = max(val, dp[i][j-1])

print(max(dp[M]))
