N, K = map(int, input().split())
A = list(map(int, input().split()))

takoyaki_val = set()
for i in range(N):
    multiA = []
    for j in range(1, K+1):
        multiA.append(j * A[i])
    print(multiA)
