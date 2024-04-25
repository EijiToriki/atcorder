N = int(input())
ans = []

J = []
for i in range(1, 10):
  if(N%i == 0):
    J.append(i)

for i in range(N+1):
  buf = []
  for j in J:
    if i % (N / j) == 0:
      buf.append(j)
  if len(buf) == 0:
    ans.append('-')
  else:
    ans.append(str(min(buf)))


print(''.join(ans))