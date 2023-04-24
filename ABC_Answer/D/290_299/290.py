from math import gcd

T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    ans = D * (K-1) % N + (K-1) // (N // gcd(N, D))
    print(ans)