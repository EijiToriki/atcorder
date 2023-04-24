num_list = [str(i) for i in range(1, 10)]

R, C = map(int, input().split())
B = []
for _ in range(R):
    B.append(list(input()))

delete_list = []
for r1 in range(R):
    for c1 in range(C):
        if B[r1][c1] in num_list:
            power = int(B[r1][c1])
            for r2 in range(R):
                for c2 in range(C):
                    if abs(r1-r2) + abs(c1-c2) <= power:
                        delete_list.append([r2, c2])

for point in delete_list:
    B[point[0]][point[1]] = '.'

for r in range(R):
    print(''.join(B[r]))
                    
