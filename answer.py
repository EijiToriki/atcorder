N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [10**18] * (N+1)

dp[1] = 0
for i in range(1, N):
    try:
        dp[i+1] = min(dp[i+1], dp[i] + A[i+1])
        dp[i+2] = min(dp[i+2], dp[i] + B[i+2])
    except IndexError:
        pass

print(dp[N])