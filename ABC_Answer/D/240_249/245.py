N, M = map(int, input().split())
A = list(reversed(list(map(int, input().split()))))
C = list(reversed(list(map(int, input().split()))))

B = []
for m in range(M+1):
    base = 0
    for n in range(N+1):
        if n == 0:
            base = C[m+n] // A[n]
            B.append(base)
        else:
            C[m+n] = C[m+n] - base*A[n]
    

print(*list(reversed((B))))