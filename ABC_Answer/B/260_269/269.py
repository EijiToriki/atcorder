S = []
for _ in range(10):
  S.append(input())

shape_i = []
shape_j = []
for i in range(10):
  for j in range(10):
    if S[i][j] == "#":
      shape_i.append(i)
      shape_j.append(j)

A, B = min(shape_i) + 1, max(shape_i) + 1
C, D = min(shape_j) + 1, max(shape_j) + 1

print(A, B)
print(C, D)