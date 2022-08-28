A  = list(map(int, input().split()))
B  = list(map(int, input().split()))
C  = list(map(int, input().split()))
D  = list(map(int, input().split()))


AB = [B[0]-A[0], B[1]-A[1]]
BC = [C[0]-B[0], C[1]-B[1]]
CD = [D[0]-C[0], D[1]-C[1]]
DA = [A[0]-D[0], A[1]-D[1]]

def is_over_180degrees(A, B):
  if A[0]*B[1] - A[1]*B[0] > 0:
    return True
  else:
    return False


if is_over_180degrees(AB, BC) and is_over_180degrees(BC, CD) and is_over_180degrees(CD, DA) and is_over_180degrees(DA, AB):
  print('Yes')
else:
  print('No')