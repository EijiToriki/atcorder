N = int(input())
S = input()

points = [[0, 0]]
buf = [0, 0]
for s in S:
    if s == 'R':
        buf[1] += 1
    elif s == 'L':
        buf[1] -= 1
    elif s == 'U':
        buf[0] += 1
    elif s == 'D':
        buf[0] -= 1
    points.append([buf[0], buf[1]])

points = sorted(points, key=lambda x:(x[0], x[1]))

for i in range(1, len(points)):
    if points[i][0] == points[i-1][0] and points[i][1] == points[i-1][1] :
        print('Yes')
        exit()
print('No')