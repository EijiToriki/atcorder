import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

ans_list = [1]
visited = set()
def dfs(v, p, ans):
  visited.add(v)
  for node in ladder[v]:
    if node == p:
      continue
    if node in visited:
      continue
    ans = max(ans, node)
    ans_list.append(ans)
    dfs(node, v, ans)
  


N = int(input())
ladder = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    ladder[a].append(b)
    ladder[b].append(a)

dfs(1, -1, 1)
print(max(ans_list))
