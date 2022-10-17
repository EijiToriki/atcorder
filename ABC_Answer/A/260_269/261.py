l1,r1,l2,r2 = map(int, input().split())

L = [i for i in range(l1,r1)]
R = [i for i in range(l2,r2)]

ans = 0
for i in L:
  if i in R:
    ans += 1

print(ans)