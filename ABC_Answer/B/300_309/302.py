H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            ## 右方向
            if j + 4 < W:
                if S[i][j+1] == 'n' and S[i][j+2] == 'u' and S[i][j+3] == 'k' and S[i][j+4] == 'e':
                    print(i+1, j+1)
                    print(i+1, j+2)
                    print(i+1, j+3)
                    print(i+1, j+4)
                    print(i+1, j+5)
                    exit()

            # 左方向
            if j - 4 >= 0:
                if S[i][j-1] == 'n' and S[i][j-2] == 'u' and S[i][j-3] == 'k' and S[i][j-4] == 'e':
                    print(i+1, j+1)
                    print(i+1, j)
                    print(i+1, j-1)
                    print(i+1, j-2)
                    print(i+1, j-3)
                    exit()

            ## 下方向
            if i + 4 < H:
                if S[i+1][j] == 'n' and S[i+2][j] == 'u' and S[i+3][j] == 'k' and S[i+4][j] == 'e':
                    print(i+1, j+1)
                    print(i+2, j+1)
                    print(i+3, j+1)
                    print(i+4, j+1)
                    print(i+5, j+1)
                    exit()
            
            ## 上方向
            if i - 4 >= 0:
                if S[i-1][j] == 'n' and S[i-2][j] == 'u' and S[i-3][j] == 'k' and S[i-4][j] == 'e':
                    print(i+1, j+1)
                    print(i, j+1)
                    print(i-1, j+1)
                    print(i-2, j+1)
                    print(i-3, j+1)
                    exit() 

            ## 右下方向    
            if i + 4 < H and j + 4 < W:
                if S[i+1][j+1] == 'n' and S[i+2][j+2] == 'u' and S[i+3][j+3] == 'k' and S[i+4][j+4] == 'e':
                    print(i+1, j+1)
                    print(i+2, j+2)
                    print(i+3, j+3)
                    print(i+4, j+4)
                    print(i+5, j+5)
                    exit()

            ## 右上方向
            if i - 4 >= 0 and j + 4 < W:
                if S[i-1][j+1] == 'n' and S[i-2][j+2] == 'u' and S[i-3][j+3] == 'k' and S[i-4][j+4] == 'e':
                    print(i+1, j+1)
                    print(i, j+2)
                    print(i-1, j+3)
                    print(i-2, j+4)
                    print(i-3, j+5)
                    exit()
            
            ## 左下方向
            if i + 4 < H and j - 4 >= 0:
                if S[i+1][j-1] == 'n' and S[i+2][j-2] == 'u' and S[i+3][j-3] == 'k' and S[i+4][j-4] == 'e':
                    print(i+1, j+1)
                    print(i+2, j)
                    print(i+3, j-1)
                    print(i+4, j-2)
                    print(i+5, j-3)
                    exit()
            
            ## 左上方向
            if i - 4 >= 0 and j - 4 >= 0:
                if S[i-1][j-1] == 'n' and S[i-2][j-2] == 'u' and S[i-3][j-3] == 'k' and S[i-4][j-4] == 'e':
                    print(i+1, j+1)
                    print(i, j)
                    print(i-1, j-1)
                    print(i-2, j-2)
                    print(i-3, j-3)
                    exit()         