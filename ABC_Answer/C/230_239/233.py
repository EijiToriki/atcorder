N, X = map(int,input().split()) 

L = []
A = []

for _ in range(N):
  al = list(map(int, input().split()))
  L.append(al[0])
  A.append(al[1:])

pro = [1]
for i in range(len(L)):
  tmp_pro = []
  for j in range(L[i]):
    for k in pro:
      tmp_pro.append(A[i][j]*k)
  pro = tmp_pro

print(pro.count(X))