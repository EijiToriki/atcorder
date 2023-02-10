## 入力受取
N = int(input())
P, A = [0], [0]
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)
P.append(0)
A.append(0)

## 変数の事前準備
dp = [[0] * 2009 for _ in range(2009)]
dp[1][N] = 0

## dp配列の更新
for LEN in range(N-2, -1, -1):
    for l in range(1, N-LEN+1):
        r = l + LEN

        score1 = 0
        if l <= P[l-1] <= r:
            score1 = A[l-1]
        score2 = 0
        if l <= P[r+1] <= r:
            score2 = A[r+1]
        
        if l == 1:
            dp[l][r] = dp[l][r+1] + score2
        elif r == N:
            dp[l][r] = dp[l-1][r] + score1
        else:
            dp[l][r] = max(dp[l-1][r]+score1, dp[l][r+1]+score2)
        

## 答え出力
ans = 0
for i in range(1, N+1):
    ans = max(ans, dp[i][i])
print(ans)

