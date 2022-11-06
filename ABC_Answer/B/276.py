N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for g in G[1:]:
  city_num = len(g)
  if city_num == 0:
    print(0)
  else:
    print(city_num, *sorted(g))
