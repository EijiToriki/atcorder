x1, y1, x2, y2 = map(int, input().split())

latis1 = []
latis2 = []

dis5_move_list = [[1,2],[2,1],[2,-1],[1,-2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

for dis5_move in dis5_move_list:
    latis1.append([x1+dis5_move[0], y1+dis5_move[1]])
    latis2.append([x2+dis5_move[0], y2+dis5_move[1]])


flag = False
for l in latis1:
    if l in latis2:
        print('Yes')
        flag = True
        break

if not flag:
    print('No')