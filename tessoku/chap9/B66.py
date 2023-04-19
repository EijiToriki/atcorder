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
A = [0] * (M+1)
B = [0] * (M+1)
for i in range(1, M+1):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

Q = int(input())
q_type = [0] * (Q+1)
x = [0] * (Q+1)
u = [0] * (Q+1)
v = [0] * (Q+1)
for i in range(1, Q+1):
    query = list(map(int, input().split()))
    q_type[i] = query[0]
    if q_type[i] == 1:
        x[i] = query[1]
    else:
        u[i] = query[1]
        v[i] = query[2]

# 運休になっている路線
cancelled = [False] * (M+1)
for i in range(1, Q+1):
    if q_type[i] == 1:
        cancelled[x[i]] = True

uf = UnionFind(N+1)
# 運休にならない路線を初めに記録
for i in range(1, M+1):
    if cancelled[i] == False and uf.same(A[i], B[i]) == False:
        uf.union(A[i], B[i])

ans = [''] * (Q+1)
# クエリを逆順処理
for i in range(Q, 0, -1):
    if q_type[i] == 1:
        if uf.same(A[x[i]], B[x[i]]) == False:
            uf.union(A[x[i]], B[x[i]])
    else:
        if uf.same(u[i], v[i]) == True:
            ans[i] = 'Yes'
        else:
            ans[i] = 'No'

for i in range(1, Q+1):
    if q_type[i] == 2:
        print(ans[i])
