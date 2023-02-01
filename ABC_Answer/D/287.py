
def match_or_not(s, t):
  if s == t or s == '?' or t == '?':
    return True
  else:
    return False


S = input()
T = input()
s_size, t_size = len(S), len(T)

head = [False] * (s_size+1)
head[0] = True
for i in range(t_size):
  if not match_or_not(S[i], T[i]):
    break
  head[i+1] = True
  
S = S[::-1]
T = T[::-1]

tail = [False] * (s_size+1)
tail[0] = True
for i in range(t_size):
  if not match_or_not(S[i], T[i]):
    break
  tail[i+1] = True

for i in range(t_size+1):
  if head[i] and tail[t_size-i]:
    print('Yes')
  else:
    print('No')
