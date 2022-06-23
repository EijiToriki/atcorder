## 全探索
N, M = map(int, input().split())

A = [list(map(int,input().split())) for _ in range(N)]

max_score = 0

# i,j は曲の選び方
for i in range(M-1):
  for j in range(i+1, M):
    score = 0
    for k in range(N):
      score += max(A[k][i],A[k][j])
    if score > max_score:
      max_score = score

print(max_score)