T = int(input())
N = int(input())

imos = [0] * (T+5)
for _ in range(N):
  l, r = map(int, input().split())
  imos[l] += 1
  imos[r] -= 1

for i in range(1, T):
  imos[i] += imos[i-1]

for i in range(T):
  print(imos[i])
