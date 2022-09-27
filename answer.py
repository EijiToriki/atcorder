N, K = map(int, input().split())
A = list(map(int, input().split()))

DP = [0] * (N+1)

for n in range(1, N+1):
    for i in range(K):
        if A[i] <= n:
            DP[n] = max(DP[n], n-DP[n-A[i]])
        else:
            break

print(DP[N])
