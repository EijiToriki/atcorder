n = int(input())
G = [[] for _ in range(n+1)]
for _ in range(n):
    u, k, *v = map(int, input().split())
    for node in v:
        G[u].append(node)

d = [1] * (n+1)
f = [1] * (n+1)


def dfs(a, b, goal):
    if a == goal:
        return None
    for to in G[a]:
        if to == b:
            continue
        d[goal] = d[goal] + 1
        print(a,b,d[goal])
        dfs(to, a, goal)

dfs(1, False, 2)

# for i in range(1, n+1):
#     dfs(1, False, i)
#     print(d)

print(d)