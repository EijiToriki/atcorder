K = int(input())

binK = str(bin(K))

ans = ''

for k in binK[2:]:
  if k == '1':
    ans += '2'
  else:
    ans += '0'

print(ans)
