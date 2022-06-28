import itertools

def judgePath(G, path):
    for i in range(1,N):
        if path[i+1] not in G[path[i]]:
            return False
    return True


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i != j:
            if [i,j] in XY or [j,i] in XY:
                pass
            else:
                G[i].append(j)

member = [i for i in range(1,N+1)]

ans_min = 10000*N
for v in itertools.permutations(member, N):
    judge_flag = judgePath(G, [0] + list(v))
    if judge_flag:
        dist_total = 0
        for i, mem in enumerate(v):
            dist_total += A[mem-1][i]
        if dist_total < ans_min:
            ans_min = dist_total

if ans_min == 10000*N:
    print(-1)
else:
    print(ans_min)