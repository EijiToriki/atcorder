def f(b):
    return (a+b)*(a**2+b**2)

N = int(input())
ans = float('INF')
for a in range(10**6+5):
    ok = 10**6+5
    ng = -1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if f(mid) >= N:
            ok = mid
        else:
            ng = mid
    ans = min(ans, f(ok))

print(ans)
