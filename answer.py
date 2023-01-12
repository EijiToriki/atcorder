# とりあえず写経した
# ダイクストラ法 → python だと TLE するっぽい
from collections import deque
import sys
from sys import stdin
input = sys.stdin.readline

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

INF = 10 ** 18

S = [[] for _ in range(H)]
for i in range(H):
    S[i] = stdin.readline()[:-1]

move_H = [1, 0, -1, 0]
move_W = [0, 1, 0, -1]

dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
deq = deque()
for i in range(4):
  dist[rs-1][cs-1][i] = 0
  deq.append((rs-1, cs-1, i))

while len(deq) != 0:
  x, y, d = deq.popleft()
  if x == rt-1 and y == ct-1:
    print(min(dist[x][y]))
    exit()
  for i in range(4):
    tx = x + move_H[i]
    ty = y + move_W[i]
    cost = dist[x][y][d] + 0
    if d != i:
      cost = dist[x][y][d] + 1
    if not (0 <= tx and tx < H and 0 <= ty and ty < W):
      continue
    if not (S[tx][ty] == '.'):
      continue
    if not (dist[tx][ty][i] > cost):
      continue

    dist[tx][ty][i] = cost
    if d != i:
      deq.append([tx, ty, i])
    else:
      deq.appendleft([tx, ty, i])

ans = float('INF')
for i in range(4):
  ans = min(ans, dist[rt-1][ct-1][i])

print(ans)