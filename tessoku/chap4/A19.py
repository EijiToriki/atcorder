## 入力受取
N, W = map(int, input().split())
Wei, Val = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    Wei.append(w)
    Val.append(v)

## 変数の事前準備
dp = [[0] * (W+1) for _ in range(N+1)]

## dp配列の更新
for i in range(1, N+1):
    for j in range(W+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j + Wei[i] <= W:
            dp[i][j+Wei[i]] = max(dp[i][j+Wei[i]], dp[i-1][j] + Val[i])

print(max(dp[N]))