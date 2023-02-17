N = int(input())
MOD = 10**9 + 7

prev1 = 1
prev2 = 1
for i in range(N-2):
    ans = (prev1 + prev2) % MOD
    prev1 = prev2 % MOD
    prev2 = ans

print(ans)

