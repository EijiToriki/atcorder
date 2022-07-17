N, X, Y = map(int, input().split())

def red(N):
  if N >= 2:
    return red(N-1) + X * blue(N)
  else:
    return 0

def blue(N):
  if N >= 2:
    return red(N-1) + Y * blue(N-1)
  else:
    return 1

print(red(N))