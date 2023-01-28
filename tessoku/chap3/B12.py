N = int(input())

def f(x):
  if x**3 + x > N:
    return True
  else:
    return False

l = 0.0
r = 50.0 * (10**6)

while l < r:
  mid = ((l+r) / (10**6)) / 2

  if f(mid):
    r = mid * (10**6) - 1
  else:
    l = mid * (10**6) + 1

print(r / (10**6))