from collections import deque, defaultdict

M = int(input())
G = [[] for _ in range(10)]

for _ in range(M):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)

s = ['9'] * 9
p = list(map(int, input().split()))
for i in range(1, 9):
  s[p[i-1]-1] = str(i)
s = ''.join(s)

qu = deque()
qu.append(s)
mp = defaultdict(str)
mp[s] = 0

while len(qu) != 0:
  s = qu.popleft()
  for i in range(1, 10):
    if s[i-1] == '9':
      v = i
  
  for u in G[v]:
    t = list(s)
    t[u-1], t[v-1] = t[v-1], t[u-1]
    t = ''.join(t)
    if t in mp.keys():
      continue
    else:
      mp[t] = mp[s] + 1
      qu.append(t)

if "123456789" not in mp.keys():
  print(-1)
else:
  print(mp['123456789'])