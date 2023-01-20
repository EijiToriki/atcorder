N = input()

ans = 0
for i, n in enumerate(reversed(N)):
  ans += int(n) * (2 ** i)

print(ans)
