import sys
A, B = input().split()

for a,b in zip(reversed(A),reversed(B)):
  keta_sum = int(a) + int(b)
  if keta_sum >= 10:
    print('Hard')
    sys.exit()

print('Easy')