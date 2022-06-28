import sys
from math import gcd

input = sys.stdin.readline

A, B = map(int, input().split())

ans = A*B // gcd(A,B)

if ans > 10**18:
    print("Large")
else:
    print(ans)
