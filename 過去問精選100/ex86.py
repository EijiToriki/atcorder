## UnionFindを利用して解く
### ある辺を取り除いた際，非連結グラフとなれば（＝集合が1つでなければ）その辺は橋
import sys
from Class.UnionFind import UnionFind

input = sys.stdin.readline
N, M = map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
a, b = [list(i) for i in zip(*ab)]

ans = 0

for i in range(M):  ## 取り除く橋
  uf = UnionFind(N)
  for j in range(M):  
    if i == j:      ## 取り除く橋を考慮しない
      continue
    uf.union(a[j]-1, b[j]-1)
  if uf.group_count() != 1:
    ans += 1

print(ans)