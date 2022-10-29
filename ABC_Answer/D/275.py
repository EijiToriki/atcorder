from functools import lru_cache
from math import floor
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=100000)
def f(n):
  if n == 0:
    return 1
  else:
    return f(floor(n/2)) + f(floor(n/3))

N = int(input())
ans = f(N)
print(ans)

