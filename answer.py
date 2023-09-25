def is_outer(row, col, N):
  if row == 0 or row == N-1:
    return True
  elif col == 0 or col == N-1:
    return True
  else:
    return False


def rotate_one_element(row, col, square, N):
  if row == 0:
    if col == 0:
      return square[row+1][col]
    else:
      return square[row][col-1]
  elif row == N - 1:
    if col == N - 1:
      return square[row-1][col]
    else:
      return square[row][col+1]
  else:
    if col == 0:
      return square[row+1][col]
    else:
      return square[row-1][col]

N = int(input())
A = []
for _ in range(N):
  A_row = input()
  A.append(A_row)

B = []
for i in range(N):
  B_row = []
  for j in range(N):
    rotate_bit = ''
    if is_outer(i, j, N):
      rotate_bit = rotate_one_element(i, j, A, N)
    else:
      rotate_bit = A[i][j]
    B_row.append(rotate_bit)
  B.append(B_row)

for B_row in B:
  print(''.join(B_row))