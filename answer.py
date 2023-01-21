N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cumsum = [0] * (N+1)
cumsum[0] = 0
for i in range(1, N+1):
  cumsum[i] = A[i-1] + cumsum[i-1]


for _ in range(Q):
  l, r = map(int, input().split())
  cnt1 = cumsum[r] - cumsum[l-1]
  if cnt1 * 2 > (r - l + 1):
    print('win')
  elif cnt1 * 2 == (r - l + 1):
    print('draw')
  else:
    print('lose')
