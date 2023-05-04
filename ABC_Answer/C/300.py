H, W = map(int, input().split())
C = [input() for _ in range(H)]

ans = [0] * (min(H, W))
used = set()

for a in range(len(ans), -1, -1):
    search_range_minH = a+1
    search_range_maxH = H-(a+1)
    search_range_minW = a+1
    search_range_maxW = W-(a+1)
    for i in range(search_range_minH, search_range_maxH):
        for j in range(search_range_minW, search_range_maxW):
            if C[i][j] == "#":
                ok = True
                for k in range(1, a+2):
                    if not(C[i+k][j+k] == "#" and C[i+k][j-k] == "#" and C[i-k][j+k] == "#" and C[i-k][j-k] == "#"):
                        ok = False
                        break
                if ok and (i, j) not in used:
                    ans[a] += 1
                    used.add((i, j))

print(*ans)
