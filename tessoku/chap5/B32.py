N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    for k in range(K):
        if i - A[k] >= 0:
            ## 勝ちパターン：負けに遷移可能
            if dp[i - A[k]] == 0:
                dp[i] = 1
                break
    ## 負けパターン：勝ちのみに遷移

if dp[N] == 1:
    print('First')
else:
    print('Second')