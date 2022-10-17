N = int(input())
MOD = 998244353

keta = len(str(N))
ans = 0

for i in range(1, keta):
  buf = (10**i-10**(i-1)) * (10**i-10**(i-1)+1) // 2
  ans = ans + buf

ans = ans + ((N-10**(keta-1)+1)*(N-10**(keta-1)+2) // 2)

print(ans%MOD)