H, W = map(int, input().split())
MOD = 1000000007

n = H + W -2
r = W - 1

fact = [0] * (n+5)
fact_inv = [0] * (n+5)
inv = [0] * (n+5)
fact[0], fact[1] = 1, 1
fact_inv[0], fact_inv[1] = 1, 1
inv[1] = 1
for i in range(2, n+5):
    fact[i] = fact[i-1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    fact_inv[i] = fact_inv[i-1] * inv[i] % MOD

ans = fact[n] * (fact_inv[r] * fact_inv[n - r] % MOD) % MOD
print(ans)
