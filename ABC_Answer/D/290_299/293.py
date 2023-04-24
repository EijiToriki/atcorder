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


N, M = map(int, input().split())

uf = UnionFind(N)
r_dict = defaultdict(int)
b_dict = defaultdict(int)

for _ in range(M):
    a, b, c, d = input().split()
    uf.union(int(a)-1, int(c)-1)
    if b == 'R':
        r_dict[int(a)-1] += 1
    else:
        b_dict[int(a)-1] += 1
    if d == 'R':
        r_dict[int(c)-1] += 1
    else:
        b_dict[int(c)-1] += 1

XY = [0, 0]
for u in uf.all_group_members().items():
    X_flag = True
    for node in u[1]:
        if r_dict[node] == 1 and b_dict[node] == 1:
            pass
        else:
            X_flag = False
            break
    if X_flag:
        XY[0] += 1
    else:
        XY[1] += 1

print(*XY)