H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
At = [list(a) for a in zip(*A)]

for Arow in At:
  print(*Arow)