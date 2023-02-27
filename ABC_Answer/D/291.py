MOD = 998244353

N = int(input())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

dp = [[0,0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
    for pre in range(2):
        for nxt in range(2):
            if AB[i-1][pre] != AB[i][nxt]:
                dp[i][nxt] += dp[i-1][pre]
    dp[i][0] %= MOD
    dp[i][1] %= MOD

ans = dp[N-1][0] + dp[N-1][1]
ans %= MOD
print(ans)