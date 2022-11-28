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


# from bisect import bisect_left
# from collections import defaultdict


# H, W, r_s, c_s = map(int, input().split())
# N = int(input())
# wall = []
# for i in range(N):
#     r, c = map(int, input().split())
#     wall.append([r, c])
# Q = int(input())
# D = []
# L = []
# for i in range(Q):
#     d, l = input().split()
#     D.append(d)
#     L.append(int(l))

# def main():
#     wall_tate_dict = defaultdict(list)
#     for i in range(len(wall)):
#         wall_tate_dict[wall[i][1]].append(wall[i][0])
#     wall_tate_dict = dict(sorted(wall_tate_dict.items()))
#     wall_tate_list = list(wall_tate_dict.keys())

#     wall_yoko_dict = defaultdict(list)        
#     for i in range(len(wall)):
#         wall_yoko_dict[wall[i][0]].append(wall[i][1])
#     wall_yoko_dict = dict(sorted(wall_yoko_dict.items()))
#     wall_yoko_list = list(wall_yoko_dict.keys())

#     print(wall_yoko_dict)
#     print(wall_tate_dict)

#     ans = [r_s, c_s]       # ans[0] たて，ans[1] よこ
#     for i in range(Q):
#         if D[i] == 'U':
#             ## 壁の処理
#             kabe_idx = bisect_left(wall_tate_list, ans[1])
#             ### 壁あり
#             if wall_tate_list[kabe_idx] == ans[1]:
#                 kabe = bisect_left(wall_tate_dict[ans[1]], ans[0])
#                 if kabe == 0:
#                     update_val = ans[0] - L[i]
#                     if update_val < 1:
#                         update_val = 1
#                 else:
#                     update_val = wall_tate_dict[ans[1]][kabe-1] + 1           
#             ### 壁無し
#             else:
#                 update_val = ans[0] - L[i]
#                 if update_val < 1:
#                     update_val = 1
#             ans = [update_val, ans[1]]

#         elif D[i] == 'D':
#             ## 壁の処理
#             kabe_idx = bisect_left(wall_tate_list, ans[1])
#             ### 壁あり
#             if wall_tate_list[kabe_idx] == ans[1]:
#                 kabe = bisect_left(wall_tate_dict[ans[1]], ans[0])
#                 if kabe == len(wall_tate_dict[ans[1]]):
#                     update_val = ans[0] + L[i]
#                     if update_val > H:
#                         update_val = H
#                 else:
#                     update_val = wall_tate_dict[ans[1]][kabe] - 1    
#             ### 壁無し
#             else:
#                 update_val = ans[0] + L[i]
#                 if update_val > H:
#                     update_val = H
#             ans = [update_val, ans[1]]

#         elif D[i] == 'L':
#             ## 壁の処理
#             kabe_idx = bisect_left(wall_yoko_list, ans[0])
#             ### 壁あり
#             if wall_yoko_list[kabe_idx] == ans[0]:
#                 kabe = bisect_left(wall_yoko_dict[ans[0]], ans[1])
#                 if kabe == 0:
#                     update_val = ans[1] - L[i]
#                     if update_val < 1:
#                         update_val = 1
#                 else:
#                     update_val = wall_yoko_dict[ans[0]][kabe-1] + 1    
#             ### 壁無し
#             else:
#                 update_val = ans[1] - L[i]
#                 if update_val < 1:
#                     update_val = 1
#             ans = [ans[0], update_val]

#         elif D[i] == 'R':
#             ## 壁の処理
#             kabe_idx = bisect_left(wall_yoko_list, ans[0])
#             ### 壁あり
#             if wall_yoko_list[kabe_idx] == ans[0]:
#                 kabe = bisect_left(wall_yoko_dict[ans[0]], ans[1])
#                 if kabe == len(wall_yoko_dict[ans[0]]):
#                     update_val = ans[1] + L[i]
#                     if update_val > W:
#                         update_val = W
#                 else:
#                     update_val = wall_yoko_dict[ans[0]][kabe] - 1    
#             ### 壁無し
#             else:
#                 update_val = ans[1] + L[i]
#                 if update_val > W:
#                     update_val = W
#             ans = [ans[0], update_val]

#         print(*ans)


 
# if __name__ == '__main__':
    
#     main()