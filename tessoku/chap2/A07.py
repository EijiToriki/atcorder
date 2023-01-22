D = int(input())
N = int(input())

imos = [0] * (D+1)
for _ in range(N):
  l, r = map(int, input().split())
  imos[l-1] += 1
  imos[r] -= 1

for i in range(1, D):
  imos[i] += imos[i-1]

for i in range(D):
  print(imos[i])