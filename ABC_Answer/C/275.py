from math import sqrt, acos, degrees, isclose

def two_vector_angle(a, b):
  bunshi = a[0]*b[0] + a[1]*b[1]
  bunbo = round(sqrt(a[0]**2+a[1]**2) * sqrt(b[0]**2+b[1]**2))
  if bunbo != 0:
    return degrees(acos(bunshi / bunbo)) 
  else:
    return -1

def check_90(A, B, C, D):
  kakuA = two_vector_angle([B[0]-A[0], B[1]-A[1]], [C[0]-A[0], C[1]-A[1]])
  kakuB = two_vector_angle([A[0]-B[0], A[1]-B[1]], [D[0]-B[0], D[1]-B[1]])
  kakuC = two_vector_angle([D[0]-C[0], D[1]-C[1]], [A[0]-C[0], A[1]-C[1]])
  kakuD = two_vector_angle([C[0]-D[0], C[1]-D[1]], [B[0]-D[0], B[1]-D[1]])

  kaku_list = [kakuA, kakuB, kakuC, kakuD]

  for kaku in kaku_list:
    if not isclose(kaku, 90):
      return False
  return True


S = []
for _ in range(9):
  S.append(input())

boan = []
for i in range(9):
  for j in range(9):
    if S[i][j] == '#':
      boan.append([i+1, j+1])

ans = 0
for a in boan:
  for b in boan:
    for c in boan:
      for d in boan:
          destAB = (a[0] - b[0])**2 + (a[1] - b[1])**2
          destBD = (b[0] - d[0])**2 + (b[1] - d[1])**2
          destDC = (d[0] - c[0])**2 + (d[1] - c[1])**2
          destAC = (a[0] - c[0])**2 + (a[1] - c[1])**2

          if destAB == 0 or destAC == 0 or destBD == 0 or destDC == 0:
            pass
          else:
            if destAB == destBD and destBD == destDC and destDC == destAC and destAC == destAB:
              if check_90(a, b, c, d):
                ans += 1

print(ans//8)

