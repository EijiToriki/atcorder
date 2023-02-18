N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

dp = [[float('INF')] * N for _ in range(2**N)]
dp[0][0] = 0
for i in range(2**N):
    for j in range(N):
        if dp[i][j] == float('INF'):
            continue
        for k in range(N):
            if (i // (2**k)) % 2 == 0:
                dist = (1.0*(X[j]-X[k])**2 + 1.0*(Y[j]-Y[k])**2)**0.5
                dp[i + (2**k)][k] = min(dp[i + (2**k)][k], dp[i][j] + dist)

print(dp[2**N-1][0])

