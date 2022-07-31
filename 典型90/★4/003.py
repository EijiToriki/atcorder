# キューのインポート
from collections import deque

# 入力の受け取り、道路情報はリストで格納
N = int(input())
G = [[] for _ in range(N)]

# 木構造作る時参考になる
for _ in range(N-1):
  A, B = map(int, input().split())
  G[A-1].append(B-1)
  G[B-1].append(A-1)

# 都市nから最も離れている都市を求める
# arr[0]：最も離れている都市番号，arr[1]：最も離れている都市の距離
def calc_min_dist(n):
  Q = deque()
  dist = [-1]*N
  dist[n] = 0
  Q.append(n)

  arr = [0, 0]

  while Q:
    i = Q.popleft()
    for j in G[i]:
      if dist[j] == -1:
        a = dist[i]+1
        dist[j] = a
        Q.append(j)
        if a > arr[1]:
          arr = [j, a]

  return arr

# １回目はノード1から呼び出し、２回目はcalc_min_distからの返り値で呼び出す。
p, dep = calc_min_dist(0)
p2, dep2 = calc_min_dist(p)

print(dep2+1) 