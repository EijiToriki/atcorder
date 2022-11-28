import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))

max_ameba = max(A)

G = [[] for _ in range(2*max_ameba+2)]

for i in range(1,N+1):
    G[A[i-1]].append(i*2)
    G[A[i-1]].append(i*2 + 1)
depth = [-1] * (2*max_ameba+2)

def dfs(v, p, d):
    depth[v] = d

    for next in G[v]:
        if next == p:
            continue
        dfs(next, v, d+1)

dfs(1, -1, 0)
for i in range(1, 2*N+2):
    print(depth[i])