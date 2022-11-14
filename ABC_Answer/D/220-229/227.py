
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

left = 0
right = 10**32

while right-left > 1:
  mid = (left + right) // 2

  sum = 0
  for i in range(N):
    sum += min(mid, A[i])
  
  if sum >= K*mid:
    left = mid
  else:
    right = mid

print(left)