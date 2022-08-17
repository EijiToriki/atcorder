import sys

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


for i in range(2**H1):
  for j in range(2**W1):
    delete_row = []
    delete_col = []
    for k in range(H1):
      if((i >> k & 1) == 0):
        delete_row.append(k)
    for k in range(W1):
      if((j >> k & 1) == 0):
        delete_col.append(k)
    
    if len(delete_row) != H2 or len(delete_col) != W2:
      continue
    
    check = True
    for k in range(H2):
      for l in range(W2):
        if(A[delete_row[k]][delete_col[l]] != B[k][l]):
          check = False
          break
    
    if check:
      print('Yes')
      sys.exit()

print('No')
