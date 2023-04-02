from bisect import bisect

N, X = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(N):
    Aj = A[i] - X
    idx = bisect(A, Aj)

    if Aj == A[idx-1]:
        print('Yes')
        exit()

print('No')
