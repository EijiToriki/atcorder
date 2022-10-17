N, X = map(int, input().split())
A = list(map(int, input().split()))

secret_set = {X}
i = X
while True:
  if A[i-1] not in secret_set:
    secret_set.add(A[i-1])
    i = A[i-1]
  else:
    break

print(len(secret_set)) 
