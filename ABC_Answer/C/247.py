import sys
sys.setrecursionlimit(10**6)

from functools import lru_cache

## メモ化再帰
@lru_cache(maxsize=None)
def C(n):
  if n == 1:
    return str(n)
  else:
    return C(n-1) + " " + str(n) + " " + C(n-1)

if __name__ == "__main__":
  N = int(input())
  print(C(N))