N, M = map(int, input().split())
A = [0]
for _ in range(M):
    a = int("".join(list(input().split())), 2)
    A.append(a)

dp = [[float('INF')] * 2**N for _ in range(M+1)]
dp[0][0] = 0
for i in range(1, M+1):
    for s in range(2**N):
        dp[i][s] = min(dp[i][s], dp[i-1][s])
        dp[i][s | A[i]] = min(dp[i][s | A[i]], dp[i-1][s] + 1)

ans = dp[M][2**N-1]
if ans == float('inf'):
    print(-1)
else:
    print(dp[M][2**N-1])
