import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1] * (N+1)

def dfs(v, c = 0):
    color[v] = c

    for next in G[v]:
        if color[next] != -1:
            if color[next] == c:
                return False
            continue
        if not dfs(next, 1-c):
            return False
    
    return True


bipartite_flag = True
for v in range(1, N+1):
    if color[v] != -1:
        continue
    if not dfs(v):
        bipartite_flag = False


if bipartite_flag:
    print('Yes')
else:
    print('No')