## とりあえず写経した
from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = []
for _ in range(H):
  sw = input()
  S.append(sw)

move_H = [1, 0, -1, 0]
move_W = [0, 1, 0, -1]

dist = [[[float('INF')] * 4 for _ in range(W)] for _ in range(H)]
deq = deque()
for i in range(4):
  dist[rs-1][cs-1][i] = 0
  deq.append([rs-1, cs-1, i])

while len(deq) != 0:
  u = deq.popleft()
  for i in range(4):
    tx = u[0] + move_H[i]
    ty = u[1] + move_W[i]
    cost = dist[u[0]][u[1]][u[2]] + 0
    if u[2] != i:
      cost = dist[u[0]][u[1]][u[2]] + 1
    if 0 <= tx and tx < H and 0 <= ty and ty < W and S[tx][ty] == '.' and dist[tx][ty][i] > cost:
      dist[tx][ty][i] = cost
      if u[2] != i:
        deq.append([tx, ty, i])
      else:
        deq.appendleft([tx, ty, i])

ans = float('INF')
for i in range(4):
  ans = min(ans, dist[rt-1][ct-1][i])

print(ans)