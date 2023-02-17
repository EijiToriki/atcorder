N = int(input())
MOD = 10000

ans = 0
for _ in range(N):
    t, a = input().split()
    a = int(a) 
    if t == '+':
        ans += a
    elif t == '-':
        ans -= a
        if ans < 0:
            ans += MOD
    else:
        ans *= a
    ans %= MOD
    print(ans)