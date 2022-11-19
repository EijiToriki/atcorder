N = int(input())

ans = ""
while N != 0:
  if N % 2 == 1:
    N = N - 1
    ans += 'A'
  else:
    N = N // 2
    ans += 'B'

ans = ''.join(reversed(ans))
print(ans)