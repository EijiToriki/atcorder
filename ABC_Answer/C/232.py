# N が 10以下のときは隣接行列で解ける
import itertools

N, M = map(int, input().split())
t_toy = [[False]*N for _ in range(N)]
a_toy = [[False]*N for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  t_toy[a-1][b-1] = True
  t_toy[b-1][a-1] = True

for _ in range(M):
  c, d = map(int, input().split())
  a_toy[c-1][d-1] = True
  a_toy[d-1][c-1] = True

ans = False
for p in itertools.permutations(range(N)):
  ok = True
  for i in range(N):
    for j in range(N):
      if t_toy[i][j] != a_toy[p[i]][p[j]]:
        ok = False

  if ok:
    ans = True

print('Yes' if ans else 'No')