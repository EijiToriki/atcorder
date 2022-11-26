H, W = map(int, input().split())
C = []
for _ in range(H):
    s = input()
    C.append(s)

grid = [[] * H for _ in range(W)]

for h in range(H):
    for w in range(W):
        grid[w].append(C[h][w])

ans = []
for i in range(W):
    cnt = 0
    for j in range(H):
        if grid[i][j] == '#':
            cnt += 1
    ans.append(cnt)

print(*ans)