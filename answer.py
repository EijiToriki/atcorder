import re

S = input()
T = input()

S = S.replace('?', '.')
T = T.replace('?', '.')

T_size = len(T)
for i in range(T_size+1):
  s = S[:i] + S[T_size+i-1:]
  res = re.match(r'(\b)' + s + r'(\b)', T)
  if res:
    print('Yes')
  else:
    print('No')