from math import sqrt

def f(g):
  try:
    return B*(g-1) + (A/sqrt(g))
  except ZeroDivisionError:
    return float('INF')
  except ValueError:
    return float('INF')

A, B = map(int, input().split())
g = int((A / (2*B)) ** (2/3))

ans = min(f(g), f(g+1), f(g-1))
print(ans)