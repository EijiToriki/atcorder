N, Q = map(int, input().split())
L = []
for _ in range(N):
    l = list(map(int, input().split()))
    L.append(l)

for _ in range(Q):
    s, t = map(int, input().split())
    print(L[s-1][t])