import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

for i in range(Q):
    x = int(input())
    mark = bisect.bisect_left(A, x)
    ans = x*mark - S[mark] + (S[N] - S[mark]) - x*(N-mark)
    print(ans)
