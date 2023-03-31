N, M = map(int, input().split())
G= [list() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N+1):
    output = ''
    output += str(i)
    output += ': {'
    output += ', '.join(map(str, G[i]))
    output += '}'
    print(output)
    