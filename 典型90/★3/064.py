import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

diff = []
ans = 0

for i in range(N-1):
    diff.append(A[i+1]-A[i])
    ans += abs(A[i+1]-A[i])

for i in range(Q):
    L, R, V = map(int, input().split())
    if L == 1 and R == N:
        pass
    elif L == 1:
        ans += abs(diff[R-1]-V) - abs(diff[R-1])
        diff[R-1] -= V
    elif R == N:
        ans += abs((diff[L-2]+V)) - abs(diff[L-2])
        diff[L-2] += V
    else:
        ans += abs(diff[R-1]-V) - abs(diff[R-1])
        diff[R-1] -= V
        ans += abs((diff[L-2]+V)) - abs(diff[L-2])
        diff[L-2] += V

    print(ans)
