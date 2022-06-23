H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = []

row = []
col = []

for i in range(H):
  row.append(sum(A[i]))

for i in range(W):
  col_sum = 0
  for j in range(H):
    col_sum += A[j][i]
  col.append(col_sum)

for i in range(H):
  B = []
  for j in range(W):
    B.append(row[i] + col[j] - A[i][j])
  print(*B)
