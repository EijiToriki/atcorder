N, K, A = map(int, input().split())

ans = A

for _ in range(K-1):
  ans += 1
  if ans > N:
    ans = 1

print(ans)
