from collections import defaultdict

usr_dict = defaultdict(str)
reverse_usr = defaultdict(list)    # 変更後に同じIDにしようとするユーザがいないかを見る辞書
visited = defaultdict(bool)       # チェック済みかを記録（ループ検知に用いる）


N = int(input())
S, T = [], []
for _ in range(N):
  s, t = input().split()
  usr_dict[s] = t
  reverse_usr[t].append(s)
  visited[s] = False

for v in reverse_usr.values():
  if len(v) != 1:
    print('No')
    exit()

for k in usr_dict.keys():
  if visited[k]:
    continue

  origin = k
  now = k
  while True:
    if now in visited:
      visited[now] = True
      now = usr_dict[now]
    else:
      break
    
    if now == origin:
      print('No')
      exit()


print('Yes')
