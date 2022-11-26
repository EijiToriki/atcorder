N, M = map(int, input().split())
X = []
for _ in range(M):
    x = list(map(int, input().split()))
    X.append(x[1:])

for n in range(1, N+1):
    participaters = set()
    for x in X:
        if n in set(x):
            for i in x:
                participaters.add(i)
    
    if len(participaters) != N:
        print('No')
        exit()

print('Yes')