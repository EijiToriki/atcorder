from math import log2

N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 10**9 + 1
while l < r:
  mid = (l + r) // 2

  ## 印刷される総数を求める
  print_num = 0
  for a in A:
    print_num += mid // a
  
  if print_num >= K:
    r = mid
  else:
    l = mid + 1

print(r)
