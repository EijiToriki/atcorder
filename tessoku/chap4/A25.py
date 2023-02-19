H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(input())

dp = [[0] * W for _ in range(H)]

for h in range(H):
    if C[h][0] == '.':
        dp[h][0] = 1
    else:
        break

for w in range(W):
    if C[0][w] == '.':
        dp[0][w] = 1
    else:
        break

for h in range(1, H):
    for w in range(1, W):
        if C[h][w] == '.':
            dp[h][w] = dp[h-1][w] + dp[h][w-1]

print(dp[H-1][W-1])
