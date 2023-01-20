N = int(input())
A = list(map(int, input().split()))

ans_flag = False
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if A[i] + A[j] + A[k] == 1000:
        ans_flag = True

if ans_flag:
  print('Yes')
else:
  print('No')