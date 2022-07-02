# 繰り返し二乗法で解く
## 選び方は，K * (K-1) * (K-2) * ... * (K-2) = K(K-1)(K-2)^(N-2)

import sys

N, K = map(int, input().split())
MOD = 10**9 + 7

if K == 1:
    if N == 1:
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()
elif N == 1:
    print(K % MOD)
    sys.exit()
elif N == 2:
    print(K*(K-1) % MOD)
else:
    ans = 1
    ans *= K % MOD
    ans *= (K-1) % MOD

    nbinary = bin(N-2)[2:]

    K_pow = (K-2)
    for i in range(len(nbinary)):
        if nbinary[len(nbinary)-i-1] == '1':
            ans = ans * K_pow % MOD
        
        K_pow = K_pow * K_pow % MOD
        

    print(ans % MOD) 