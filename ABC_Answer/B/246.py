import math
A, B = map(int, input().split())

distance = math.sqrt(A*A+B*B)
singleA = A / distance
singleB = B / distance

print(str(singleA) + " " + str(singleB))
