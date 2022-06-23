import sys
N, Y = map(int, input().split())

for i in range(N+1):
  for j in range(N+1):
    k = N - (i+j)
    if k >= 0:
      otoshidama = i*1000 + j*5000 + k*10000
      if otoshidama == Y and i+j+k == N:
        print(*[k,j,i])
        sys.exit()
    if i+j+k > N:
      break
  if i+j+k > N:
    break

print(*[-1,-1,-1])