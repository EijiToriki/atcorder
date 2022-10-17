import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

for _ in range(Q):
  xi = int(input())
  xi_idx = bisect.bisect_left(A, xi)
  print(N-xi_idx)