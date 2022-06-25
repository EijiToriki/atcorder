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

N = int(input())
xyp = [map(int, input().split()) for _ in range(N)]
X, Y, P = [list(i) for i in zip(*xyp)]

max_jump = max(P)
max_jump_index = P.index(max(P))

minS = 10**9
for i in range(N):
    if i != max_jump_index:
        S = (abs(X[i] - X[max_jump_index]) + abs(Y[i] - Y[max_jump_index])) // max_jump
        if S < minS:
            minS = S

while True:
    uf = UnionFind(N)

    for i in range(N):
        for j in range(N):
            if i!= j:
                if P[i]*minS >= abs(X[i] - X[j]) + abs(Y[i] - Y[j]):
                    uf.union(i,j)

    if uf.group_count() == 1:
        break   

    minS += 1

print(minS)



