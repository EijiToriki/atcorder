import sys

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]

xy_cnt = 0
for i in range(N-1):
  T -= A[i]
  if T <= 0:
    print('No')
    sys.exit()

  if xy_cnt < len(xy):
    if i+1 == xy[xy_cnt][0] - 1:
      T += xy[xy_cnt][1]
      xy_cnt += 1

print('Yes')  
