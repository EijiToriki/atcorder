## 入力受取
S = 'a' + input()
T = 'b' + input()

## 変数の事前準備
dp = [[0] * (len(T)) for _ in range(len(S))]

## dp配列の更新
for i in range(1, len(S)):
    for j in range(1, len(T)):
        if S[i] == T[j]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

## 答え出力
ans = dp[len(S)-1][len(T)-1]
print(ans)

