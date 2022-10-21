import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

depth = [-1] * (N+1)
subtree_size = [-1] * (N+1)

def dfs(v, p, d):
    depth[v] = d

    for next in G[v]:
        if next == p:
            continue
        dfs(next, v, d+1)
    
    subtree_size[v] = 1
    for next in G[v]:
        if next == p:
            continue
        subtree_size[v] += subtree_size[next]


dfs(1, -1, 0)
for i in range(1, N+1):
    print('Node {:0>3} depth : {:0>3}, children : {:0>3}'.format(i, depth[i], subtree_size[i]))