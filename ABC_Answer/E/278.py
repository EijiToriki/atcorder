from collections import defaultdict

H, W, N, h, w = map(int, input().split())
A = []
for _ in range(H):
  A.append(list(map(int, input().split())))

i_dict = defaultdict(list)
j_dict = defaultdict(list)

for i in range(H):
  for j in range(W):
    i_dict[A[i][j]].append(i)
    j_dict[A[i][j]].append(j)

minmax_dict = defaultdict(list)   # key: a (1,...,N), [0]: minX, [1]: maxX, [2]: minY, [3]: maxY

kind_N = 0
for a in range(1, N+1):
  try:
    minmax_dict[a].append(min(i_dict[a]))
    minmax_dict[a].append(max(i_dict[a]))
    minmax_dict[a].append(min(j_dict[a]))
    minmax_dict[a].append(max(j_dict[a]))
    kind_N += 1
  except ValueError:
    pass

ans_h = H - h + 1
ans_w = W - w + 1

ans = []
for k in range(ans_h):
  row = []
  for l in range(ans_w):
    reduce_cnt = 0
    for a in range(1, N+1):
      try:
        if k <= minmax_dict[a][0] and minmax_dict[a][1] < k+h and l <= minmax_dict[a][2] and minmax_dict[a][3] < l+w:
          reduce_cnt += 1
      except IndexError:
        pass
    row.append(kind_N-reduce_cnt)
  ans.append(row)

for row in ans:
  print(*row)
