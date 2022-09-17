W = int(input())
W = 10 ** 6

ans = [i for i in range(1,100)]

for i in range(100,100**2, 100):
  ans.append(i)

for i in range(100**2, 100**3, 100**2):
  ans.append(i)

ans.append(W)

print(len(ans))
print(*ans)