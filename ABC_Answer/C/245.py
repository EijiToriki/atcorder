N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

resultFlag = 1

currentA = 1
currentB = 1
futureA = 0
futureB = 0


for i in range(N-1):
  if currentA == 1:
    if abs(A[i] - A[i+1]) <= K:
      futureA = 1
    if abs(A[i] - B[i+1]) <= K:
      futureB = 1
  
  if currentB == 1:
    if abs(B[i] - A[i+1]) <= K:
      futureA = 1
    if abs(B[i] - B[i+1]) <= K:
      futureB = 1
  
  if futureA == 0 and futureB == 0:
    resultFlag = 0
    break
  else:
    currentA = futureA
    currentB = futureB
    futureA = 0
    futureB = 0

if resultFlag == 0:
  print("No")
else:
  print("Yes") 