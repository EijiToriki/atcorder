N = int(input())
A = sorted(map(int, input().split()))
sumA = sum(A)
divA = sumA // len(A)
amariA = sumA % len(A)

ideal = []
for i in range(N):
  if i < amariA:
    ideal.append(divA+1)
  else:
    ideal.append(divA)

ideal = sorted(ideal)

ans = 0
for i in range(N):
  ans += abs(ideal[i] - A[i])
ans //= 2

print(ans)