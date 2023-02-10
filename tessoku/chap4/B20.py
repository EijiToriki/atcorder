## 入力受取
S = input()
T = input()

## 変数の事前準備
lenS, lenT = len(S), len(T)
dp = [[0] * (lenT+1) for _ in range(lenS+1)]

## コーナーケースへの対応
if S == T:
    print(0)
    exit()
if S == '':
    print(lenT)
    exit()
if T == '':
    print(lenS)
    exit()

## dp配列の更新
for i in range(lenS+1):
    dp[i][0] = i
for j in range(lenT+1):
    dp[0][j] = j

for i in range(1, lenS+1):
    sc = S[i-1]
    for j in range(1, lenT+1):
        tc = T[j-1]
        cost = 0 if (sc==tc) else 1
        dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)

## 答え出力
ans = dp[lenS][lenT]
print(ans)

