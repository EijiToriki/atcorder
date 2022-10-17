import sys

N = int(input())
S = [input() for _ in range(N)]

basic_num = 6

for i in range(N):
  for j in range(N):
    if j < N-basic_num+1:
      yoko = S[i][j] + S[i][j+1] + S[i][j+2] + S[i][j+3] + S[i][j+4] + S[i][j+5]
      if yoko.count('#') >= 4:
        print('Yes')
        sys.exit()
    
    if i < N-basic_num+1:
      tate = S[i][j] + S[i+1][j] + S[i+2][j] + S[i+3][j] + S[i+4][j] + S[i+5][j]
      if tate.count('#') >= 4:
        print('Yes')
        sys.exit()
    
    if j < N-basic_num+1 and i < N-basic_num+1:
      miginaname = S[i][j] + S[i+1][j+1] + S[i+2][j+2] + S[i+3][j+3] + S[i+4][j+4] + S[i+5][j+5]
      if miginaname.count('#') >= 4:
        print('Yes')
        sys.exit()
    
    if j >= basic_num-1 and i < N-basic_num+1:
      hidarinaname = S[i][j] + S[i+1][j-1] + S[i+2][j-2] + S[i+3][j-3] + S[i+4][j-4] + S[i+5][j-5]
      if hidarinaname.count('#') >= 4:
        print('Yes')
        sys.exit()

print('No')