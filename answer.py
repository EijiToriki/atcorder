N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]

path = []
for i in range(N):
  buf = []
  for j in range(M):
    if i == G[j][0]-1:
      buf.append(G[j][1]-1)
  path.append(buf)


d = [0]*(N+1) # 最初に発見した時刻
f = [0]*(N+1) # 隣接リストを調べ終えた時刻

TIME = 0

def dfs(p, d, f):
   global TIME

   # ここに来訪時の処理を書く
   TIME += 1
   d[p] = TIME # 時刻の記録
   
   for nxt in path[p]: #繋がってる点の内 
       if d[nxt] == 0: # 未探索の(発見時刻が初期値のままの場合)
           dfs(nxt, d, f) # 先に進む
   
   # ここに帰る時の処理を書く
   TIME += 1
   f[p] = TIME # 繋がってる全ての点を探索し終えたらその点でやることは終わり
   
   return     
   
for start in range(N):
   if d[start] == 0: # 未探索の点があれば
       dfs(start, d, f) # dfs開始

for i in range(1, N+1):
   print(i, d[i], f[i])


