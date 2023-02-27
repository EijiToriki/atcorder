N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = B * (N*M) + sum(A) * M + sum(C) * N
print(ans)