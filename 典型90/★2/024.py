N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_query_cnt = 0
for a,b in zip(A,B):
  min_query_cnt += abs(a-b)

if min_query_cnt == K:
  print('Yes')
elif min_query_cnt < K:
  if (K-min_query_cnt) % 2 == 0:
    print('Yes')
  else:
    print('No')
else:
  print('No')
