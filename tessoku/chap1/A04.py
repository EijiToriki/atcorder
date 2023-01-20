N = int(input())

ans = bin(N)[2:]
for _ in range(len(ans), 10):
  ans = '0' + ans

print(ans)