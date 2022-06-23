N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result1 = 0
result2 = 0

for i in range(N):
  if A[i] == B[i]:
    result1 += 1
  elif A[i] in B:
    result2 += 1

print(result1)
print(result2)