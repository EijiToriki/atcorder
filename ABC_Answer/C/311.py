import sys
sys.setrecursionlimit(10**6)

def detect_cycle(graph):
  def dfs(node, parent):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
      if not visited[neighbor]:
        parent[neighbor] = node
        if dfs(neighbor, parent):
          return True
      elif rec_stack[neighbor]:
        current_node = node
        display_path(parent, current_node, neighbor)

    rec_stack[node] = False
    return False

  def display_path(parent, current_node, neighbor):
    cycle = []
    while current_node != neighbor:
      cycle.append(current_node)
      current_node = parent[current_node]
    cycle.append(neighbor)
    cycle = list(reversed(cycle))
    print(len(cycle))
    print(*cycle)
    exit()

  num_nodes = len(graph)
  visited = [False] * num_nodes
  rec_stack = [False] * num_nodes

  for node in range(num_nodes):
      if not visited[node]:
          parent = [-1] * num_nodes
          if not dfs(node, parent):
              continue

  print("閉路は見つかりませんでした.")

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N+1)]

for i in range(N):
  G[i+1].append(A[i])

detect_cycle(G)