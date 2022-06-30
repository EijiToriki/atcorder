## 動的計画法で解く
## N 段目の上り方は，その一個前の上り方と，L個前の上り方の合計である

N, L = map(int, input().split())
MOD = 10**9 + 7

dp = [0 for _ in range(N+1)]

dp[0] = 1

for i in range(1,N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i-L]) % MOD

print(dp[N])