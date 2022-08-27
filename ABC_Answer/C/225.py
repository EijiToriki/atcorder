N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans_flag = True
for i in range(N):
  amari = B[i][0] % 7
  if amari == 0:
    amari = 7

  for j in range(1, M):
    if B[i][j] - B[i][j-1] != 1:
      ans_flag = False
    
    new_amari = B[i][j] % 7
    if new_amari == 0:
      new_amari = 7
    
    if new_amari < amari:
      ans_flag = False
    else:
      amari = new_amari

for i in range(M):
  for j in range(1, N):
    if B[j][i] - B[j-1][i] != 7:
      ans_flag = False

if ans_flag:
  print('Yes')
else:
  print('No')