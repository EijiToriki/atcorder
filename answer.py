N, C = input().split()
A = input()

red_num = 0
blue_num = 0

for a in A:
    if a == 'R':
        red_num += 1
    if a == 'B':
        blue_num += 1

color = ''
if red_num > blue_num:
    color = 'R'
elif red_num == blue_num:
    color = 'W'
else:
    color = 'B'

if color == C:
    print('Yes')
else:
    print('No')



10  0
8   1
6   2
4   3
2   4
0   5