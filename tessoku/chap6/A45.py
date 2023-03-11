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
    red_num -= blue_num
    if red_num % 3 == 1:
        color = 'R'
    elif red_num % 3 == 2:
        color = 'B'
    else:
        color = 'W'

elif red_num == blue_num:
    color = 'W'
else:
    blue_num -= red_num
    if blue_num % 3 == 1:
        color = 'B'
    elif blue_num % 3 == 2:
        color = 'R'
    else:
        color = 'W'
        

if color == C:
    print('Yes')
else:
    print('No')
