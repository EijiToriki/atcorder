n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n):
    u, k, *v = map(int, input().split())
    for node in v:
        G[u].append(node)

d = [1] * (n+1)
f = [1] * (n+1)
visited = [False] * (n+1)
TIME = 0


def dfs(a):
    global TIME

    TIME += 1
    d[a] = TIME

    visited[a] = True

    for to in G[a]:
        if visited[to] == False:
            dfs(to)
    
    TIME += 1
    f[a] = TIME


for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)

for i in range(1, n+1):
    print(i, d[i], f[i])
