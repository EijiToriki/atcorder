N, S = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
