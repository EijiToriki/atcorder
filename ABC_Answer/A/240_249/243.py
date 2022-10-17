V, A, B, C = map(int, input().split())

cnt = 0

while True:
  if cnt%3 == 0:
    V = V - A
  if cnt%3 == 1:
    V = V - B
  if cnt%3 == 2:
    V = V - C
  
  if V < 0:
    if cnt%3 == 0:
      print('F')
    if cnt%3 == 1:
      print('M')
    if cnt%3 == 2:
      print('T')
    break
  cnt += 1