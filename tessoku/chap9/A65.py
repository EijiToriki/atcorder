N = int(input())
A = [0, 0] + list(map(int, input().split()))

G = [[] for _ in range(N+1)]
for i in range(2, N+1):
    G[A[i]].append(i)

dp = [0] * (N+1)
for i in range(N, 0, -1):
    for j in range(len(G[i])):
        dp[i] += (dp[G[i][j]] + 1)

print(*dp[1:])