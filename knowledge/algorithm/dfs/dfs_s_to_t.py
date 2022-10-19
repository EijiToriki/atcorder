N, M, s, t = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)

visited = [False] * (N+1)

def dfs(node):
    visited[node] = True

    for to in G[node]:
        if visited[to] == False:
            dfs(to)
    
dfs(s)
if visited[t]:
    print('Yes')
else:
    print('No')
