N = int(input())
S = input()

for i in range(1, N):
  l = 0
  k = 0
  while True:
    if l + i >= N:
      break
    if S[k] != S[k+i]:
      l += 1
      k += 1
    else:
      break
  print(l)
