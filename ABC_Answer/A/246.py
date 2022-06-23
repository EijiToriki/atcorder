xy = [map(int, input().split()) for _ in range(3)]
xEdge, yEdge = [list(i) for i in zip(*xy)]

x3 = 0
y3 = 0

for xa in xEdge:
  cnt = 0
  for xb in xEdge:
    if xa == xb:
      cnt += 1
  if cnt == 1:
    x3 = xa
    break

for ya in yEdge:
  cnt = 0
  for yb in yEdge:
    if ya == yb:
      cnt += 1
  if cnt == 1:
    y3 = ya
    break

print(str(x3) + " " + str(y3))
