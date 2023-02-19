N = int(input())
for_cnt = 0
for _ in range(N):
  s = input()
  if s == 'For':
    for_cnt += 1

if N // 2 < for_cnt:
  print('Yes')
else:
  print('No')