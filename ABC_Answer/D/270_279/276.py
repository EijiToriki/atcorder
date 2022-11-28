from functools import reduce
from math import gcd

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def more_gcd(*numbers):
    return reduce(gcd, numbers)

N = int(input())
A = list(map(int, input().split()))

target = more_gcd(*A)

ans = 0
for a in A:
  a_div_target = a // target
  pfs = factorization(a_div_target)   # pf = prime factor
  for pf in pfs:
    if pf[0] == 1 and pf[1] == 1:
      break
    if pf[0] == 2 or pf[0] == 3:
      ans += pf[1]
    else:
      print(-1)
      exit()

print(ans)
