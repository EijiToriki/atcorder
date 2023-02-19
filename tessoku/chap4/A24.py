from bisect import bisect_left

N = int(input())
A = [0] + list(map(int, input().split()))

dp = [1] * (N+1)
L = [0] + [10**18] * N

dp[1] = 1
L[1] = A[1]
for i in range(2, N+1):
    l_idx = bisect_left(L, A[i])    
    dp[i] = l_idx
    L[l_idx] = A[i]

ans = max(dp)
print(ans)
