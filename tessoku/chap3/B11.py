from bisect import bisect_left

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

for _ in range(Q):
  x = int(input())
  ans = bisect_left(A, x)
  print(ans)
