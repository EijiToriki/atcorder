from math import gcd

A, B = map(int, input().split())
ans = gcd(A, B)
print(ans)