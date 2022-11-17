N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
  res = 0
  now_len = 1
  change_flag = False
  for i in range(1, N):
    if change_flag:
      change_flag = False
      continue
    if A[i] == A[i-1]:
      now_len += 1
      if now_len > x:
        res += 1
        now_len = 1
        change_flag = True
    else:
      now_len = 1
  return res <= K


left = 0
right = N
while right-left > 1:
  mid = (left + right) // 2
  if check(mid):
    right = mid
  else:
    left = mid

print(right)