import sys

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

now = A[0]
now_cnt = 1
for i in range(1,len(A)):
  if now == A[i]:
    now_cnt += 1
  else:
    if now_cnt != 4:
      print(now)
      sys.exit()
    now = A[i]
    now_cnt = 1

if now_cnt != 4:
  print(A[i])