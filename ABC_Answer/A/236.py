S = input()
a,b = map(int, input().split())

sa = S[a-1]
sb = S[b-1]
ans = ''

for i in range(len(S)):
  if i == a-1:
    ans += sb
  elif i == b-1:
    ans += sa
  else:
    ans += S[i]

print(ans)