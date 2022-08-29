S = input()
S = list(S)

ans = 0
idx = S.index('a')
for i in range(idx, 0, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

idx = S.index('t')
for i in range(idx, 1, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

idx = S.index('c')
for i in range(idx, 2, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

idx = S.index('o')
for i in range(idx, 3, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

idx = S.index('d')
for i in range(idx, 4, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

idx = S.index('e')
for i in range(idx, 5, -1):
  S[i], S[i-1] = S[i-1], S[i]
  ans += 1

print(ans)
