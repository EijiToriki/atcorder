N = int(input())
A = list(map(int, input().split()))

alice = 0
bob = 0

A = sorted(A, reverse=True)

for i in range(N):
  if i%2 == 0:
    alice += A[i]
  else:
    bob += A[i]

print(alice-bob)


