import math

T = int(input())
for _ in range(T):
  N = int(input())
  p, q = 0, 0
  i = 2
  while i <= N**(1/3):
    if N % i != 0:
      i += 1
      continue
    else:
      if N % i**2 == 0:
        p = i
        q = int(N // i**2)
        break
      else:
        q = i
        p = int(math.sqrt(N // i))
        break

  print("{} {}".format(p, q))

