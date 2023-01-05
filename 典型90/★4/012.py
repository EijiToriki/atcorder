from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

H, W = map(int, input().split())
Q = int(input())
used = [[False] * 2010 for _ in range(2010)]
uf = UnionFind(W*H)

def query1(px, py):
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  for i in range(4):
    sx, sy = px + dx[i], py + dy[i]
    if used[sx][sy] == False:
      continue
    hash1 = (px - 1) * W + (py - 1)
    hash2 = (sx - 1) * W + (sy - 1)
    uf.union(hash1, hash2)

  used[px][py] = True


def query2(px, py, qx, qy):
  if used[px][py] == False or used[qx][qy] == False:
    return False
  
  hash1 = (px - 1) * W + (py - 1)
  hash2 = (qx - 1) * W + (qy - 1)
  if uf.same(hash1, hash2):
    return True
  else:
    return False

for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    query1(query[1], query[2])
  else:
    if query2(query[1], query[2], query[3], query[4]):
      print('Yes')
    else:
      print('No')
