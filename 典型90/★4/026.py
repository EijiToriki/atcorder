import sys
sys.setrecursionlimit(10**6)


N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1] * (N+1)

def dfs(v, c = 0):
    color[v] = c

    for next in G[v]:
        if color[next] != -1:
            if color[next] == c:
                return False
            continue
        if not dfs(next, 1-c):
            return False
    
    return True

dfs(1)
num0 = color.count(0)
num1 = color.count(1)
ans_num = N // 2
ans_list = []
if num0 >= num1:
  cnt = 0
  for i in range(len(color)):
    if color[i] == 0:
      ans_list.append(i)
      cnt += 1
    if cnt == ans_num:
      break
else:
  cnt = 0
  for i in range(len(color)):
    if color[i] == 1:
      ans_list.append(i)
      cnt += 1
    if cnt == ans_num:
      break

print(*ans_list)
