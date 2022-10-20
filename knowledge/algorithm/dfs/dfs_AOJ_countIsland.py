import sys
sys.setrecursionlimit(10**6)

island = []
move_list = [-1, 0, 1]

def dfs(h, w):
    island[h][w] = 0

    for dh in move_list:
        for dw in move_list:
            nh, nw = h + dh, w + dw

            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if island[nh][nw] == 0:
                continue
        
            dfs(nh, nw)


ans = 0

while True:
    W, H = map(int, input().split())
    if H == 0 and W == 0:
        break


    island = []

    for h in range(H):
        line = list(map(int, input().split()))
        island.append(line)
    
    ans = 0
    for h in range(H):
        for w in range(W):
            if island[h][w] == 0:
                continue
            dfs(h, w)
            ans += 1
        
    print(ans)
