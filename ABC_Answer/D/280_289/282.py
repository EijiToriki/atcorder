## https://zenn.dev/yamasakit/articles/05ddc577bbf78b より拝借
import sys


sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append(v)
    G[v].append(u)

colors = [-1] * N
done = [False] * N
groups = {}


def dfs(v, color, root):
    colors[v] = color
    done[v] = True
    groups[root][color] += 1
    for to in G[v]:
        if colors[to] == color:
            return False
        if colors[to] == -1 and not dfs(to, color ^ 1, root):
            return False
    return True


for i in range(N):
    if done[i]:
        continue
    groups[i] = [0, 0]  # num_black, num_white
    is_bipartite = dfs(i, 0, i)
    if not is_bipartite:
        print(0)
        exit()

# Group 内
group_in = 0
for num_black, num_white in groups.values():
    group_in += num_black * num_white
group_in -= M

# Group 外
group_out = 0
for num_black, num_white in groups.values():
    v = num_black + num_white
    group_out += v * (N - v)

ans = group_in + group_out // 2
print(ans)


## TLE 満載 と WA 2つの回答
### 模解確認後，自分で書いたコード
# import sys
# sys.setrecursionlimit(10**6)

# from collections import defaultdict

# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         if self.parents[x] > self.parents[y]:
#             x, y = y, x

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         group_members = defaultdict(list)
#         for member in range(self.n):
#             group_members[self.find(member)].append(member)
#         return group_members

#     def __str__(self):
#         return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# N, M = map(int, input().split())
# G = [[] for _ in range(N+1)]
# uf = UnionFind(N)

# for _ in range(M):
#   u, v = map(int, input().split())
#   G[u].append(v)
#   G[v].append(u)
#   uf.union(u-1, v-1)

# color = [-1] * (N+1)
# def judge_binary_graph(v, c = 0):
#     color[v] = c

#     for next in G[v]:
#         if color[next] != -1:
#             if color[next] == c:
#                 return False
#             continue
#         if not judge_binary_graph(next, 1-c):
#             return False
    
#     return True


# ans = (N * (N-1)) // 2 - M
# for members in uf.all_group_members().values():
#   bipartite_flag = True
#   for v in members:
#     v = v+1
#     if color[v] != -1:
#         continue
#     if not judge_binary_graph(v):
#         bipartite_flag = False

  
#   if bipartite_flag:
#     cnt0 = color.count(0)
#     cnt1 = color.count(1)
#     ans -= (((cnt0 * (cnt0-1)) // 2) + ((cnt1 * (cnt1-1)) // 2))
#   else:
#     ans = 0
#     print(ans)
#     exit()

# print(ans)