L, R = map(int, input().split())
S = input()

ans = ''
for i in range(len(S)):
  if i >= L-1 and i <= R-1:
    ans += S[R+L-i-2]
  else:
    ans += S[i]

print(ans)
