import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
        

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
uf = UnionFind(N)

for _ in range(M):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)
  uf.union(u-1, v-1)

color = [-1] * (N+1)
def judge_binary_graph(v, c = 0):
    color[v] = c

    for next in G[v]:
        if color[next] != -1:
            if color[next] == c:
                return False
            continue
        if not judge_binary_graph(next, 1-c):
            return False
    
    return True


ans = (N * (N-1)) // 2 - M
for members in uf.all_group_members().values():
  bipartite_flag = True
  for v in members:
    v = v+1
    if color[v] != -1:
        continue
    if not judge_binary_graph(v):
        bipartite_flag = False

  
  if bipartite_flag:
    cnt0 = color.count(0)
    cnt1 = color.count(1)
    ans -= (((cnt0 * (cnt0-1)) // 2) + ((cnt1 * (cnt1-1)) // 2))
  else:
    ans = 0
    print(ans)
    exit()

print(ans)