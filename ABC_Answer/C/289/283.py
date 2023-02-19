S = input()
ans = 0
prev = False
for i in range(len(S)):
  if S[i] == '0':
    if prev:
      ans += 1
      prev = False
    else:
      prev = True
  else:
    if prev:
      ans += 2
    else:
      ans += 1
    prev = False

if prev:
  ans += 1

print(ans)