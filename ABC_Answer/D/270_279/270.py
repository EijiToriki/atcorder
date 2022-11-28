N, K = map(int, input().split())
A = list(map(int, input().split()))

DP = [0] * (N+1)

for i in range(1, N+1):
    for k in range(K):
        if A[i] <= k:
            DP[i] = max(DP[i], i-DP[i-A[i-1]])
        else:
            break

print(DP[N])
