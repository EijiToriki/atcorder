N, T = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)

repeat_num = T // sumA
T = T - (sumA * repeat_num)

for i, a in enumerate(A):
  T = T - a
  if T < 0:
    ans = [i + 1, a + T]
    break

print(*ans)