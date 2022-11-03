def make_diagram(S):
  diagram = []
  for i in range(N):
    for j in range(N):
      if S[i][j] == '#':
        diagram.append((i,j))

  x_list = []
  y_list = []
  for d in diagram:
    x_list.append(d[0])
    y_list.append(d[1])

  x_min, y_min = min(x_list), min(y_list)

  start_diagram = []
  for d in diagram:
    start_diagram.append((d[0]-x_min, d[1]-y_min))

  return start_diagram


def judge_same_digaram(S, T):
  if len(S) != len(T):
    return False
  for s, t in zip(S, T):
    if s[0] == t[0] and s[1] == t[1]:
      pass
    else:
      return False
  return True

N = int(input())
S, T = [], []
for _ in range(N):
  S.append(input())

for _ in range(N):
  T.append(input())

S90, S180, S270 = [], [], []
for s in zip(*S[::-1]):
  S90.append(''.join([*s]))

for s in zip(*S90[::-1]):
  S180.append(''.join([*s]))

for s in zip(*S180[::-1]):
  S270.append(''.join([*s]))

diagram_T = make_diagram(T)
diagram_S = make_diagram(S)
diagram_S90 = make_diagram(S90)
diagram_S180 = make_diagram(S180)
diagram_S270 = make_diagram(S270)

if judge_same_digaram(diagram_T, diagram_S):
  print('Yes')
  exit()

if judge_same_digaram(diagram_T, diagram_S90):
  print('Yes')
  exit()

if judge_same_digaram(diagram_T, diagram_S180):
  print('Yes')
  exit()

if judge_same_digaram(diagram_T, diagram_S270):
  print('Yes')
  exit()

print('No')