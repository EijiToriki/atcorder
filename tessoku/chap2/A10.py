N = int(input())
A = [0] + list(map(int, input().split()))

cummax_L = [0] * (N+1)
cummax_R = [0] * (N+1)

for i in range(1, N+1):
  cummax_L[i] = max(cummax_L[i-1], A[i])

for i in range(1, N+1):
  cummax_R[i] = max(cummax_R[i-1], A[N-i+1])
cummax_R = [0] + list(reversed(cummax_R[1:]))

## クエリに回答
D = int(input())
for _ in range(D):
  l, r = map(int, input().split())
  ans = max(cummax_L[l-1], cummax_R[r+1])
  print(ans)