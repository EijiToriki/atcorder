MOD = 10**9 + 7

H, W = map(int, input().split())
A = []
for _ in range(H):
    row = input()
    A.append(row)

dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            continue
        try:
            if A[i][j+1] == '.':
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= MOD
        except IndexError:  # 場外に行ってしまうのを防ぐ
            pass
        try:
            if A[i+1][j] == ".":
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD
        except IndexError:  # 場外に行ってしまうのを防ぐ
            pass

print(dp[H-1][W-1])