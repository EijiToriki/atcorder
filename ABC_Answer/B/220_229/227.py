def f(a, b):
  return 4*a*b + 3*a + 3*b

N = int(input())
S = list(map(int, input().split()))

ans = N
for n in range(N):
  flag = False
  for a in range(1,1000):
    for b in range(1,1000):
      if f(a,b) == S[n]:
        ans -= 1
        flag = True
        break
    if flag:
      break

print(ans)
    
