N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
  A, B = map(int, input().split())
  G[A-1].append(B-1)
  G[B-1].append(A-1)

ans = 0
for i in range(len(G)):
  for j in G[i]:
    for k in G[j]:
      if i in G[k]:
        ans += 1
print(ans//6)