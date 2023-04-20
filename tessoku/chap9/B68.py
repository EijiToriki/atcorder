class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F
    used[pos] = True
    for e in G[pos]:
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            if flow >= 1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    return 0


def maxflow(N, s, t, edges):
    G = [list() for _ in range(N + 3)]
    offset = 0

    for i in range(1, N+1):
        if P[i] >= 0:
            G[N+1].append(maxflow_edge(i, P[i], len(G[i])))
            G[i].append(maxflow_edge(N+1, 0, len(G[N+1])-1))
            offset += P[i]
        else:
            G[i].append(maxflow_edge(N+2, -P[i], len(G[N+2])))
            G[N+2].append(maxflow_edge(i, 0, len(G[i])-1))

    for a, b in edges:
        G[a].append(maxflow_edge(b, 10**18, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a])-1))
    INF = 10 ** 10
    total_flow = 0
    while True:
        used = [False] * (N+3)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break
    return offset - total_flow


N, M = map(int, input().split())
P = [0] + list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

ans = maxflow(N, N+1, N+2, edges)
print(ans)