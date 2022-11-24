N, Q = map(int, input().split())

front = [-1] * (N+1)
back = [-1] * (N+1)

for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    back[query[1]] = query[2]
    front[query[2]] = query[1]
  elif query[0] == 2:
    back[query[1]] = -1
    front[query[2]] = -1
  else:
    root = query[1]
    while front[root] != -1:
      root = front[root]
    ans = [root]
    child = root
    while back[child] != -1:
      child = back[child]
      ans.append(child)
    print(len(ans), *ans)