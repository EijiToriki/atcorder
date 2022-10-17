N = int(input())
A = list(map(int, input().split()))
A = set(A)

result = -1
for i in range(N+1):
  if i not in A:
    result = i
    break

print(result)