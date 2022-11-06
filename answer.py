from functools import reduce
from math import gcd

def more_gcd(*numbers):
    return reduce(gcd, numbers)

N = int(input())
A = list(map(int, input().split()))

target = more_gcd(*A)


ans = 0
for a in A:
  while True:
    if a == target:
      break
    if a % 3 == 0:
      a = a // 3
    elif a % 2 == 0:
      a = a // 2
    else:
      print(-1)
      exit()
    ans += 1

print(ans)
