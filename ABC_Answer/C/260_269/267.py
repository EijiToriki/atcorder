import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]

sumi = [-float('INF')]*(N-M+1)
now = 0
for i in range(M):
    now += A[i]*(i+1)
sumi[0] = now

for i in range(1, N-M+1):
    sumi[i] = sumi[i-1]+M*A[M+i-1]-(S[M+i-1]-S[i-1])

ans = -sys.maxsize
for i in range(N-M+1):
    ans = max(ans, sumi[i])

print(ans)
