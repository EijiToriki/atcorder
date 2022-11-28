from collections import defaultdict

N, Q = map(int, input().split())
user = defaultdict(set)

for _ in range(Q):
  t, a, b = map(int, input().split())
  if t == 1:
    user[a].add(b)
  elif t == 2:
    try:
      user[a].remove(b)
    except KeyError:
      pass
  elif t == 3:
    if b in user[a] and a in user[b]:
      print('Yes')
    else:
      print('No')
    

