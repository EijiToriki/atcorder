N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumsum = [0] * (N+1)
cumsum[0] = 0

for i in range(1, N+1):
  cumsum[i] = A[i-1] + cumsum[i-1]


for _ in range(Q):
  l, r = map(int, input().split())
  ans = cumsum[r] - cumsum[l-1]
  print(ans)
