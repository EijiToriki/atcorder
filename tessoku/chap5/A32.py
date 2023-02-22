N, A, B = map(int, input().split())

dp = [0] * (N+1)

for i in range(A):
    dp[i] = 0

for i in range(A, N+1):
    ## 勝ちパターン
    if dp[i-A] == 0:
        dp[i] = 1
    if i - B >= 0 and dp[i-B] == 0:
        dp[i] = 1
    ## 負けパターン
    if dp[i-A] == 1 and dp[i-B] == 1:
        dp[i] = 0

if dp[N] == 1:
    print('First')
else:
    print('Second')