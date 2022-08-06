N = int(input())
P = list(map(int, input().split()))

ans = 0
p = N
while True:
  p = P[p-2]
  ans += 1
  if p == 1:
    break

print(ans)