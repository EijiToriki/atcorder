N = int(input())
T = input()

x = 0
y = 0

rCnt = 0

for t in T:
  if t == 'S':
    if rCnt%4 == 0:
      x += 1
    if rCnt%4 == 1:
      y -= 1
    if rCnt%4 == 2:
      x -= 1
    if rCnt%4 == 3:
      y += 1
  if t == 'R':
    rCnt += 1

print(str(x) + " " + str(y))