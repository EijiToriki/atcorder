from bisect import bisect_left

N, K = map(int, input().split())
A = list(map(int, input().split()))

half_N = N // 2
former = []
for i in range(2**half_N):
  val = 0
  for j in range(half_N):
    if ((i >> j) & 1):
      val += A[j]
  former.append(val)
former = sorted(former)

latter = []
for i in range(2**(N-half_N)):
  val = 0
  for j in range(N-half_N):
    if ((i >> j) & 1):
      val += A[half_N + j]
  latter.append(val)
latter = sorted(latter)

for f in former:
  search_num = K - f
  search_idx = bisect_left(latter, search_num)
  try:
    if latter[search_idx] == search_num:
      print('Yes')
      exit()  
  except IndexError:
    pass

print('No')
