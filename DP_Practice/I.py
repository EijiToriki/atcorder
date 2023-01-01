N = int(input())
P = list(map(float, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N)]

dp[0][0] = 1 - P[0]
dp[0][1] = P[0]

for i in range(1, N):
    for j in range(i+1):
        dp[i][j] += dp[i-1][j] * (1 - P[i])
        dp[i][j+1] += dp[i-1][j] * P[i]


ans = 0
j_prime = N // 2 + 1
for j in range(j_prime, N+1):
    ans += dp[N-1][j]

print(ans)