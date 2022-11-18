N, A, B = map(int, input().split())
H = []
for _ in range(N):
  H.append(int(input()))

A -= B
left = 0
right = 10**10

while right-left > 1:
  mid = (left + right) // 2
  
  life_B = []     # mid回爆発させた後に生き残っている魔物のhp
  for i in range(N):
    if H[i] - mid * B > 0:
      life_B.append(H[i] - mid * B)
    
  cnt_A = 0
  for i in range(len(life_B)):
    if life_B[i] % A == 0:
      cnt_A += (life_B[i] // A)
    else:
      cnt_A += (life_B[i] // A + 1)
  
  if cnt_A <= mid:
    right = mid
  else:
    left = mid

print(right)