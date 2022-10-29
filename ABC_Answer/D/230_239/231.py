import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

def check_child_cnt(G):
  for node in G:
    if len(node) > 2:
      return False
  return True


visited = [False]*(N+1)
finished = [False]*(N+1)
def check_dfs(v, p, pos):
  visited[v] = True
  for next in G[v]:
    if next == p:
      continue
    if finished[next]:
      continue
    if visited[next] and (not finished[next]):
      pos = next
      return False
    
    check_dfs(next, v, pos)

    if pos != -1:
      return False
    
  finished[v] = True
  return True


if not check_child_cnt(G):
  print('No')
  exit()

for i in range(1, N+1):
  pos = -1
  if not visited[i]:
    if not check_dfs(i, False, pos):
      print('No')
      exit()

print('Yes')
