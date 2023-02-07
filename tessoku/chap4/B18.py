## 入力受取
N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))

## 変数の事前準備
maxS = 10**4 + 5
dp = [[0] * (maxS) for _ in range(N+1)]
dp[0][0] = 1

## dp配列の更新
for i in range(1, N+1):
    for j in range(maxS):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            if j + A[i] < maxS:
                dp[i][j+A[i]] = 1

if dp[N][S] != 1:
    print(-1)
    exit()

ans = []
now = S
for i in range(N, 0, -1):
    if dp[i-1][now] == 0 and dp[i-1][now-A[i]] == 1:
        now = now - A[i]
        ans.append(i)

ans.reverse()
print(len(ans))
print(*ans)