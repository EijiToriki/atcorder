from bisect import bisect_left


H, W, r_s, c_s = map(int, input().split())
N = int(input())
wall = []
for i in range(N):
    r, c = map(int, input().split())
    wall.append([r, c])
Q = int(input())
D = []
L = []
for i in range(Q):
    d, l = input().split()
    D.append(d)
    L.append(int(l))

def main():
    wall_tate = sorted(wall, key=lambda x:x[1])
    wall_tate_only = [r[1] for r in wall_tate]
    wall_yoko = sorted(wall, key=lambda x:x[0])
    wall_yoko_only = [r[0] for r in wall_yoko]

    print(wall_tate)
    print(wall_yoko)

    ans = [r_s, c_s]       # ans[0] たて，ans[1] よこ
    for i in range(Q):
        if D[i] == 'U':
            ## 壁の処理
            kabe = bisect_left(wall_tate_only, ans[1])
            max_val = 0
            while True:
                try:
                    if wall_tate[kabe][1] == ans[1]:
                        if max_val < wall_tate[kabe][0]:
                            max_val = wall_tate[kabe][0]
                    else:
                        break
                except IndexError:
                    break
                kabe += 1
            

            update_val = ans[0] - L[i]
            if max_val == 0 and ans[0] > max_val:
                if update_val <= max_val:
                    update_val = max_val + 1
            ####
            if update_val < 1:
                update_val = 1
            ans = [update_val, ans[1]]

        elif D[i] == 'D':
            ## 壁の処理
            kabe = bisect_left(wall_tate_only, ans[1])
            min_val = H+1
            while True:
                try:
                    if wall_tate[kabe][1] == ans[1]:
                        if min_val > wall_tate[kabe][0]:
                            min_val = wall_tate[kabe][0]
                    else:
                        break
                except IndexError:
                    break
                kabe += 1
            
            update_val = ans[0] + L[i]
            if min_val == H+1 and ans[0] < min_val:
                if update_val >= min_val:
                    update_val = min_val + 1
            ####

            if update_val > H:
                update_val = H
            ans = [update_val, ans[1]]

        elif D[i] == 'L':
            ## 壁の処理
            kabe = bisect_left(wall_yoko_only, ans[0])
            max_val = 0
            while True:
                try:
                    if wall_yoko[kabe][0] == ans[0]:
                        if max_val < wall_yoko[kabe][1]:
                            max_val = wall_yoko[kabe][1]
                    else:
                        break
                except IndexError:
                    break
                kabe += 1
            
            update_val = ans[1] - L[i]
            if max_val == 0 and ans[1] > max_val:
                if update_val <= max_val:
                    update_val = max_val + 1
            ####
            
            if update_val < 1:
                update_val = 1 
            ans = [ans[0], update_val]

        elif D[i] == 'R':
            ## 壁の処理
            kabe = bisect_left(wall_yoko_only, ans[0])
            min_val = W+1
            while True:
                try:
                    if wall_yoko[kabe][0] == ans[0]:
                        if min_val > wall_yoko[kabe][1]:
                            min_val = wall_yoko[kabe][1]
                    else:
                        break
                except IndexError:
                    break
                kabe += 1

            update_val = ans[1] + L[i]

            if min_val == W+1 and ans[1] < min_val:
                if update_val >= min_val:
                    update_val = min_val + 1
            ####

            if update_val > W:
                update_val = W
            ans = [ans[0], update_val]

        print(*ans)


 
if __name__ == '__main__':
    
    main()