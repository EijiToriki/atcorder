A, B = map(int, input().split())

ans_flag = False
for i in range(A, B+1):
  if 100 % i == 0:
    ans_flag = True
    break

if ans_flag:
  print('Yes')
else:
  print('No')
