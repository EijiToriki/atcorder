n, a, x, y = map(int, input().split())

if n >= a:
    ans = x * a + (n - a) * y
else:
    ans = x * n

print(ans)