from math import sqrt, acos, degrees, isclose
 
A  = list(map(int, input().split()))
B  = list(map(int, input().split()))
C  = list(map(int, input().split()))
D  = list(map(int, input().split()))
 
def two_vector_angle(a, b):
  bunshi = a[0]*b[0] + a[1]*b[1]
  bunbo = sqrt(a[0]**2+a[1]**2) * sqrt(b[0]**2+b[1]**2)
  return degrees(acos(bunshi / bunbo)) 
 
kakuA = two_vector_angle([B[0]-A[0], B[1]-A[1]], [D[0]-A[0], D[1]-A[1]])
kakuB = two_vector_angle([C[0]-B[0], C[1]-B[1]], [A[0]-B[0], A[1]-B[1]])
kakuC = two_vector_angle([D[0]-C[0], D[1]-C[1]], [B[0]-C[0], B[1]-C[1]])
kakuD = two_vector_angle([A[0]-D[0], A[1]-D[1]], [C[0]-D[0], C[1]-D[1]])

kaku_list = [kakuA, kakuB, kakuC, kakuD]

if isclose(sum(kaku_list), 360.0):
  print('Yes')
else:
  print('No')