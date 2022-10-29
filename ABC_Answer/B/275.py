A, B, C, D, E, F = map(int, input().split())
MOD = 998244353

ans = ((A*B*C) - (D*E*F)) % MOD 
print(ans)