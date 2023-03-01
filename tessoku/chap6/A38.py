D, N = map(int, input().split())
LRH = []
for _ in range(N):
    l, r, h = map(int, input().split())
    LRH.append([l, r, h])

dp = [24] * (D+1)
for i in range(N):
    for j in range(1, D+1):
        if LRH[i][0] <= j <= LRH[i][1]:
            dp[j] = min(dp[j], LRH[i][2])

ans = sum(dp) - dp[0]
print(ans)