from collections import defaultdict

H, W, N, h, w = map(int, input().split())
A = []
for _ in range(H):
  A.append(list(map(int, input().split())))

color = defaultdict(int)

for i in range(H):
  for j in range(W):
    color[A[i][j]] += 1


ans_h = H - h + 1
ans_w = W - w + 1

ans = []
for k in range(ans_h):
  row = []
  for l in range(ans_w):
    new_color = color.copy()
    for m in range(h):
      for n in range(w):
        new_color[A[k+m][l+n]] -= 1
        if new_color[A[k+m][l+n]] == 0:
          del new_color[A[k+m][l+n]]
    row.append(len(new_color))
  ans.append(row)


for row in ans:
  print(*row)

